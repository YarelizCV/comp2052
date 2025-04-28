from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from flask_principal import Principal, Permission, RoleNeed, Identity, identity_changed, identity_loaded, AnonymousIdentity, UserNeed
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'clave_super_secreta'

# Configuración login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Configuración roles
principals = Principal(app)

# Permisos
admin_permission = Permission(RoleNeed('admin'))
user_permission = Permission(RoleNeed('user'))

# Base de datos simulada
users = {
    'juan': {
        'password': generate_password_hash('adminpass'),
        'role': 'admin'
    },
    'Yareliz': {
        'password': generate_password_hash('yarepass'),
        'role': 'user'
    }
}

# Clase User
class User(UserMixin):
    def __init__(self, username):
        self.id = username
        self.role = users[username]['role']

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None

@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    identity.user = current_user
    if hasattr(current_user, 'id'):
        identity.provides.add(UserNeed(current_user.id))
        identity.provides.add(RoleNeed(current_user.role))

# Rutas
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = users.get(username)
        if user and check_password_hash(user['password'], password):
            user_obj = User(username)
            login_user(user_obj)
            identity_changed.send(app, identity=Identity(user_obj.id))
            if user_obj.role == 'admin':
                return redirect(url_for('admin'))
            else:
                return redirect(url_for('user'))
        else:
            flash('Credenciales inválidas', 'danger')
    return render_template('login.html')

@app.route('/admin')
@login_required
@admin_permission.require(http_exception=403)
def admin():
    return render_template('admin.html', nombre=current_user.id)

@app.route('/user')
@login_required
@user_permission.require(http_exception=403)
def user():
    return render_template('user.html', nombre=current_user.id)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    identity_changed.send(app, identity=AnonymousIdentity())
    flash('Sesión cerrada exitosamente', 'info')
    return redirect(url_for('login'))

@app.errorhandler(403)
def unauthorized(e):
    return render_template('unauthorized.html'), 403

if __name__ == '__main__':
    app.run(debug=True)
