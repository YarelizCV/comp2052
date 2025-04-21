from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

app = Flask(__name__)

app.config["SECRET_KEY"] = "mi_clave_secreta"

# Crear formulario de registro
class RegistrationForm(FlaskForm):
    name = StringField("Nombre", validators=[DataRequired(), Length(min=3, message="El nombre debe tener al menos 3 caracteres.")])
    email = StringField("Correo", validators=[DataRequired(), Email(message="Correo inválido.")])
    password = PasswordField("Contraseña", validators=[DataRequired(), Length(min=6, message="La contraseña debe tener al menos 6 caracteres.")])
    confirm_password = PasswordField("Confirmar Contraseña", validators=[DataRequired(), EqualTo('password', message="Las contraseñas deben de ser iguales.")])
    submit = SubmitField("Registrar")

@app.route("/", methods=["GET", "POST"])
def index():
    form = RegistrationForm()  # Crea el formulario de registro
    if form.validate_on_submit():  
        return redirect(url_for("success"))  # Envia a la ruta de sucess
    return render_template("index.html", form=form)

@app.route("/success")
def success():
    return "<h1>Se ha registrado con éxito</h1>"

if __name__ == "__main__":
    app.run(debug=True)