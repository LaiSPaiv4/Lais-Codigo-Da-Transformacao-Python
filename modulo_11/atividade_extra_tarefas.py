import sqlite3

BANCO = "modulo_11/sistema.db"


def conectar():
    """Abre a conexão com o banco de dados."""
    return sqlite3.connect(BANCO)


def inicializar_tabela_tarefas():
    """Cria a tabela de tarefas caso ela ainda não exista."""
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = """
        CREATE TABLE IF NOT EXISTS Tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Pendente'
        );
        """
        cursor.execute(sql)
        conexao.commit()

    except sqlite3.Error as e:
        print(f"❌ Erro ao inicializar tabela de tarefas: {e}")

    finally:
        conexao.close()


# ADICIONAR TAREFA
def adicionar_tarefa(titulo):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "INSERT INTO Tarefas (titulo) VALUES (?)"
        cursor.execute(sql, (titulo,))

        conexao.commit()
        print(f"\n>> Tarefa '{titulo}' adicionada com sucesso!")

    except sqlite3.Error as e:
        print(f"Erro ao adicionar tarefa: {e}")

    finally:
        conexao.close()


# VISUALIZAR TAREFAS
def listar_tarefas():
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "SELECT id, titulo, status FROM Tarefas"
        cursor.execute(sql)
        resultados = cursor.fetchall()

        if not resultados:
            print("\nNenhuma tarefa cadastrada por enquanto.")
            return

        print("\n" + "=" * 50)
        print(f"{'ID':<5} | {'TAREFA':<25} | {'STATUS'}")
        print("=" * 50)
        for t_id, titulo, status in resultados:
            # Coloca um emoji bonitinho dependendo do status da tarefa
            emoji = "⏳" if status == "Pendente" else "✅"
            print(f"{t_id:<5} | {titulo:<25} | {emoji} {status}")
        print("=" * 50)

    except sqlite3.Error as e:
        print(f"❌ Erro ao listar tarefas: {e}")

    finally:
        conexao.close()


# EXCLUIR TAREFA
def excluir_tarefa(tarefa_id):
    try:
        conexao = conectar()
        cursor = conexao.cursor()

        sql = "DELETE FROM Tarefas WHERE id = ?"
        cursor.execute(sql, (tarefa_id,))

        conexao.commit()

        if cursor.rowcount > 0:
            print(f"\n>> Tarefa ID {tarefa_id} excluída com sucesso!")

        else:
            print(f"\nNenhuma tarefa encontrada com o ID {tarefa_id}.")

    except sqlite3.Error as e:
        print(f"❌ Erro ao excluir tarefa: {e}")

    finally:
        conexao.close()


def menu():
    inicializar_tabela_tarefas()

    while True:
        print("\n📝 GESTOR DE TAREFAS - ATIVIDADE EXTRA\n")
        print("1. Adicionar Nova Tarefa")
        print("2. Visualizar Todas as Tarefas")
        print("3. Excluir Tarefa")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            titulo = input("Digite a descrição da tarefa: ")
            if titulo.strip():
                adicionar_tarefa(titulo)
            else:
                print("⚠️ O título da tarefa não pode ser vazio!")

        elif opcao == "2":
            listar_tarefas()

        elif opcao == "3":
            listar_tarefas()  
            t_id = input("Digite o ID da tarefa que deseja excluir: ")
            if t_id.isdigit():
                excluir_tarefa(int(t_id))
            else:
                print("⚠️ ID inválido! Digite apenas números.")

        elif opcao == "0":
            print("\nSaindo do gerenciador de tarefas... Até mais!")
            break

        else:
            print("⚠️ Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()