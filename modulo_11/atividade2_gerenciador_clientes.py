import sqlite3

BANCO = "modulo_11/sistema.db"

def conectar():
    return sqlite3.connect(BANCO)

# Inserir - (CREATE)
def inserir_cliente(nome, email):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO Clientes (nome, email) VALUES (?, ?)", (nome, email))
        conexao.commit()
        print(f"\nCliente '{nome}' cadastrado com sucesso!")

    except sqlite3.IntegrityError:
        print("\nErro: Este e-mail já está cadastrado!")

    finally:
        conexao.close()


# Consultar tudo - (READ)
def listar_clientes():
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, nome, email FROM Clientes")
        resultados = cursor.fetchall()

        if not resultados:
            print("\n Nenhum cliente cadastrado ainda.")
            return

        print("\n" + "=" * 60)
        print(f"{'ID':<5} | {'NOME':<20} | {'EMAIL'}")
        print("=" * 60)
        for c_id, nome, email in resultados:
            print(f"{c_id:<5} | {nome:<20} | {email}")
        print("=" * 60)

    finally:
        conexao.close()


# Atualizar - (UPDATE)
def atualizar_cliente(c_id, novo_email):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("UPDATE Clientes SET email = ? WHERE id = ?", (novo_email, c_id))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"\nE-mail do ID {c_id} atualizado para '{novo_email}'!")

        else:
            print(f"\nID {c_id} não encontrado.")

    finally:
        conexao.close()


# Deletar - (DELETE)
def deletar_cliente(c_id):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM Clientes WHERE id = ?", (c_id,))
        conexao.commit()

        if cursor.rowcount > 0:
            print(f"\nCliente ID {c_id} removido com sucesso!")

        else:
            print(f"\nID {c_id} não encontrado.")

    finally:
        conexao.close()

def menu():
    while True:
        print("\nSISTEMA DE GERENCIAMENTO DE CLIENTES (CRUD)\n")
        print("1. Cadastrar Cliente")
        print("2. Listar Todos os Clientes")
        print("3. Atualizar E-mail")
        print("4. Excluir Cliente")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            email = input("E-mail: ")
            inserir_cliente(nome, email)

        elif opcao == "2":
            listar_clientes()

        elif opcao == "3":
            c_id = input("ID do cliente: ")
            novo_email = input("Novo e-mail: ")
            if c_id.isdigit(): atualizar_cliente(int(c_id), novo_email)

        elif opcao == "4":
            c_id = input("ID para excluir: ")
            if c_id.isdigit(): deletar_cliente(int(c_id))

        elif opcao == "0":
            break

        else:
            print("⚠️ Opção inválida.")


if __name__ == "__main__":
    menu()