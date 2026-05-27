from flask import Flask, jsonify

app = Flask(__name__)

# Uma rota simples que devolve uma mensagem de sucesso
@app.route('/api/status', methods=['GET'])
def obter_status():
    return jsonify({"status": "operando", "mensagem": "API funcionando perfeitamente!"}), 200

if __name__ == '__main__':
    app.run(debug=True)