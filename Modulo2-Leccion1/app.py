from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

DATA_FILE = 'productos.json'

def cargar_productos():
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_productos(productos):
    with open(DATA_FILE, 'w') as f:
        json.dump(productos, f, indent=4)

@app.route('/')
def index():
    productos = cargar_productos()
    return render_template('index.html', productos=productos)

@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if request.method == 'POST':
        productos = cargar_productos()
        nuevo = {
            "id": len(productos) + 1,
            "nombre": request.form['nombre'],
            "precio": float(request.form['precio']),
            "categoria": request.form['categoria']
        }
        productos.append(nuevo)
        guardar_productos(productos)
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    productos = cargar_productos()
    producto = next((p for p in productos if p["id"] == id), None)
    if request.method == 'POST':
        producto['nombre'] = request.form['nombre']
        producto['precio'] = float(request.form['precio'])
        producto['categoria'] = request.form['categoria']
        guardar_productos(productos)
        return redirect(url_for('index'))
    return render_template('edit.html', producto=producto)

if __name__ == '__main__':
    app.run(debug=True)
