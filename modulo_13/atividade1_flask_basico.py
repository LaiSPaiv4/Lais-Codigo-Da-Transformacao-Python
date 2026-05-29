from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Servidor ativo! Coloque /saudacao no final do link do seu navegador."

@app.route('/saudacao', methods=['GET'])
def saudacao():
    return jsonify({
        "mensagem": "Ola! Seja bem-vindo a API do Modulo 13."
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)