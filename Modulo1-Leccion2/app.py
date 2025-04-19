from flask import Flask, request , jsonify

app = Flask(__name__)


@app.route('/info', methods= ['GET'])
def info():
    return jsonify({
        "nombre": "Mi primera aplicacion con Flask",
        "version":"1.0",
        "descripcion": "Esta es una aplicacion de ejemplo usando Flask creada por Yareliz"
    })

@app.route('/mensaje', methods=['POST'])
def mensaje():
    data = request.get_json()
    respuesta= {"mensaje": f"Bienvenida, {data['nombre']}! Su mensaje fue recibido."}
    return jsonify(respuesta)

if __name__ == "__main__":
    app.run(debug=True)