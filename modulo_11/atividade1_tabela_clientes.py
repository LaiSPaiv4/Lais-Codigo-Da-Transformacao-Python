import sqlite3

BANCO = "modulo_11/sistema.db"

def criar_banco_e_tabela():
    conexao = None
    try:
        conexao = sqlite3.connect(BANCO)
        cursor = conexao.cursor()

        sql_tabela = """
        CREATE TABLE IF NOT EXISTS Clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        );
        """
        cursor.execute(sql_tabela)
        conexao.commit()
        
        print("=" * 45)
        print("🎉 Banco de dados 'sistema.db' configurado!")
        print("📋 Tabela 'Clientes' criada com sucesso.")
        print("=" * 45)

    except sqlite3.Error as e:
        print(f"❌ Erro ao criar o banco: {e}")
    finally:
        if conexao:
            conexao.close()

if __name__ == "__main__":
    criar_banco_e_tabela()