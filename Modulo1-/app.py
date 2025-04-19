from flask import Flask, request, jsonify

app= Flask (__name__)

# Estructura para almacenar datos
usuario = []

# Ruta GET para obtner informacion del sistema
@app.route('/info', methods= ['GET'])
def info():
    return jsonify({
        'descripcion': 'Gestor de usuarios',
        'version': '1.0',
        'autor': 'Yareliz Catalan'
    })

# Ruta POST para crear un nuevo usuario
@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    data= request.get_json()

    nombre= data.get('nombre')
    correo = data.get('correo')

    #Validacion de datos
    if not nombre or not correo:
        return jsonify ({'error': 'Faltan datos: nombre y correo son obligatorios. '})
    
    usuario.append({'nombre': nombre, 'correo': correo})
    return jsonify({'mensaje': 'Usuario creado exitosamente. '})

# Ruta GET para obtener la lista de usuarios
@app.route('/usuario', methods=['GET'])
def obtener_usuario():
    return jsonify(usuario)

if __name__ == '__main__':
    app.run(debug=True)
