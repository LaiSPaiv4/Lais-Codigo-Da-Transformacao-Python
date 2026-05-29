# Modulo_13/atividade_3.py
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_NAME = "usuarios.db"

# Conectar ao SQLite para criar a tabela se não existir
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/saudacao', methods=['GET'])
def saudacao():
    return jsonify({"mensagem": "Olá! Servidor com banco de dados ativo."}), 200

# Rota POST que persiste os dados no SQLite de verdade
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    data = request.get_json()
    
    if not data or 'nome' not in data or 'email' not in data:
        return jsonify({"erro": "Dados inválidos. Envie 'nome' e 'email'."}), 400
    
    nome = data['nome']
    email = data['email']
    
    try:
        # Integre o servidor Flask a um banco de dados SQLite para armazenar as informações
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (nome, email) VALUES (?, ?)", (nome, email))
        conn.commit()
        conn.close()
        
        return jsonify({"mensagem": f"Usuário {nome} salvo no SQLite com sucesso!"}), 201
        
    except sqlite3.IntegrityError:
        return jsonify({"erro": "Este email já está cadastrado no banco de dados."}), 400
    except Exception as e:
        return jsonify({"erro": f"Erro interno: {str(e)}"}), 500

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5002)