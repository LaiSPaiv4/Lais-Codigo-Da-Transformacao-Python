from flask import Flask, request, jsonify
import sqlite3
import secrets

app = Flask(__name__)
DB_BLOG = "blog.db"

# --- CONFIGURAÇÃO DO BANCO DE DADOS ---
def init_blog_db():
    conn = sqlite3.connect(DB_BLOG)
    cursor = conn.cursor()
    # Tabela de Usuários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            senha TEXT NOT NULL,
            token TEXT
        )
    ''')
    # Tabela de Posts
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            conteudo TEXT NOT NULL,
            autor_id INTEGER,
            FOREIGN KEY(autor_id) REFERENCES usuarios(id)
        )
    ''')
    # Tabela de Comentários
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comentarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT NOT NULL,
            post_id INTEGER,
            autor_id INTEGER,
            FOREIGN KEY(post_id) REFERENCES posts(id),
            FOREIGN KEY(autor_id) REFERENCES usuarios(id)
        )
    ''')
    conn.commit()
    conn.close()

# --- FUNÇÃO AUXILIAR DE AUTENTICAÇÃO ---
def obter_usuario_por_token():
    token = request.headers.get('Authorization')
    if not token:
        return None
    conn = sqlite3.connect(DB_BLOG)
    cursor = conn.cursor()
    cursor.execute("SELECT id, username FROM usuarios WHERE token = ?", (token,))
    user = cursor.fetchone()
    conn.close()
    return user  # Retorna (id, username) ou None

# --- ROTA INICIAL DO BLOG ---
@app.route('/', methods=['GET'])
def index():
    return "API do Blog Ativa! Use as rotas /auth/registrar, /auth/login, /posts e /posts/<id>/comentarios", 200

# --- ROTAS DE AUTENTICAÇÃO ---

@app.route('/auth/registrar', methods=['GET', 'POST'])
def registrar():
    if request.method == 'GET':
        return "A rota de registro está ativa! Para criar um usuário, envie os dados (username e senha) via POST (JSON).", 200
        
    data = request.get_json()
    if not data or 'username' not in data or 'senha' not in data:
        return jsonify({"erro": "Envie 'username' e 'senha' no formato JSON."}), 400
    try:
        conn = sqlite3.connect(DB_BLOG)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (username, senha) VALUES (?, ?)", (data['username'], data['senha']))
        conn.commit()
        conn.close()
        return jsonify({"mensagem": "Usuário do blog registrado com sucesso!"}), 201
    except sqlite3.IntegrityError:
        return jsonify({"erro": "Este username já existe."}), 400

@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return "A rota de login está ativa! Envie suas credenciais via POST (JSON) para receber seu Token de acesso.", 200

    data = request.get_json()
    if not data:
        return jsonify({"erro": "Envie seus dados de login."}), 400

    username = data.get('username')
    senha = data.get('senha')
    
    conn = sqlite3.connect(DB_BLOG)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM usuarios WHERE username = ? AND senha = ?", (username, senha))
    user = cursor.fetchone()
    
    if user:
        # Gera um token aleatório e seguro para autenticação simulada
        token = secrets.token_hex(16)
        cursor.execute("UPDATE usuarios SET token = ? WHERE id = ?", (token, user[0]))
        conn.commit()
        conn.close()
        return jsonify({
            "mensagem": "Login realizado com sucesso!", 
            "token": token
        }), 200
    
    conn.close()
    return jsonify({"erro": "Credenciais inválidas."}), 401

# --- ROTAS DE POSTS ---

@app.route('/posts', methods=['GET', 'POST'])
def gerenciar_posts():
    if request.method == 'POST':
        user = obter_usuario_por_token()
        if not user:
            return jsonify({"erro": "Não autorizado. Envie o token no Header 'Authorization'."}), 401
            
        data = request.get_json()
        if not data or 'titulo' not in data or 'conteudo' not in data:
            return jsonify({"erro": "Envie 'titulo' e 'conteudo' do post."}), 400
            
        conn = sqlite3.connect(DB_BLOG)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO posts (titulo, conteudo, autor_id) VALUES (?, ?, ?)", (data['titulo'], data['conteudo'], user[0]))
        conn.commit()
        conn.close()
        return jsonify({"mensagem": "Post criado com sucesso!"}), 201

    # Se for GET, lista todos os posts criados (Pode abrir direto no navegador)
    conn = sqlite3.connect(DB_BLOG)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT posts.id, posts.titulo, posts.conteudo, usuarios.username 
        FROM posts 
        JOIN usuarios ON posts.autor_id = usuarios.id
    """)
    posts = [{"id": r[0], "titulo": r[1], "conteudo": r[2], "autor": r[3]} for r in cursor.fetchall()]
    conn.close()
    return jsonify(posts), 200

# --- ROTAS DE COMENTÁRIOS ---

@app.route('/posts/<int:post_id>/comentarios', methods=['GET', 'POST'])
def gerenciar_comentarios(post_id):
    if request.method == 'POST':
        user = obter_usuario_por_token()
        if not user:
            return jsonify({"erro": "Não autorizado. Envie o token no Header 'Authorization'."}), 401
            
        data = request.get_json()
        if not data or 'texto' not in data:
            return jsonify({"erro": "Envie o campo 'texto' com o seu comentário."}), 400
            
        conn = sqlite3.connect(DB_BLOG)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO comentarios (texto, post_id, autor_id) VALUES (?, ?, ?)", (data['texto'], post_id, user[0]))
        conn.commit()
        conn.close()
        return jsonify({"mensagem": "Comentário adicionado com sucesso!"}), 201

    # Se for GET, lista os comentários do post correspondente (Pode abrir no navegador)
    conn = sqlite3.connect(DB_BLOG)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT comentarios.id, comentarios.texto, usuarios.username 
        FROM comentarios 
        JOIN usuarios ON comentarios.autor_id = usuarios.id 
        WHERE comentarios.post_id = ?
    """, (post_id,))
    comentarios = [{"id": r[0], "texto": r[1], "autor": r[2]} for r in cursor.fetchall()]
    conn.close()
    return jsonify(comentarios), 200

if __name__ == '__main__':
    init_blog_db()  # Garante que as tabelas do blog sejam criadas
    app.run(debug=True, port=5003)