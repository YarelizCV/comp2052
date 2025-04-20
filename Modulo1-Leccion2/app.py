from flask import Flask, request , jsonify

app = Flask(__name__)

#Ruta GET /info
@app.route('/info', methods= ['GET'])
def info():
    return jsonify({
        "nombre": "Servidor Capstone",
        "descripcion": "Esta es una aplicacion de API REST"
    })

#Ruta POST /mensaje
@app.route('/mensaje', methods=['POST'])
def mensaje_recibido():
    print('Metodo recibido:', request.method)

    if request.method == 'POST':
        data = request.get_json()
        nombre = data.get('nombre', 'invitado')
        mensaje = data.get('mensaje', '')
        return jsonify ({
            "respuesta": f"Hola, {nombre}. Se ha recibido su mensaje: '{mensaje}' "
        })
    else:
        return jsonify({
            "mensaje": "Debe utilizar POST para poder enviar un mensaje."
        })

if __name__ == "__main__":
    app.run(debug=True)