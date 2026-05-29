from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota de saudação da atividade 1 (mantida para o projeto ficar completo)
@app.route('/saudacao', methods=['GET'])
def saudacao():
    return jsonify({
        "mensagem": "Olá! Seja bem-vindo à API do Módulo 13."
    }), 200

# Rota da Atividade 2: Cadastro de usuários recebendo dados via JSON
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    # Se você acessar pelo navegador, vai cair aqui (GET)
    if request.method == 'GET':
        return "A rota /cadastrar está ativa! Para enviar dados de verdade, use uma requisição POST com JSON.", 200
        
    # Se for um envio de dados (POST), processa o JSON
    data = request.get_json()
    
    # Validação dos campos obrigatórios
    if not data or 'nome' not in data or 'email' not in data:
        return jsonify({"erro": "Dados inválidos. Envie 'nome' e 'email' no formato JSON."}), 400
        
    nome = data['nome']
    email = data['email']
    
    # Retorna o JSON de sucesso exigido pela atividade
    return jsonify({
        "mensagem": f"Usuário {nome} recebido com sucesso (Simulação de Cadastro)!",
        "usuario": {
            "nome": nome,
            "email": email
        }
    }), 201

if __name__ == '__main__':
    # Rodando na porta 5001 para não dar conflito com a atividade 1
    app.run(debug=True, port=5001)