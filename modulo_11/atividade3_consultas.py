import sqlite3

BANCO = "modulo_11/sistema.db"

def buscar_por_inicial(letra):
    """Filtra clientes cujo nome começa com uma letra específica."""
    try:
        conexao = sqlite3.connect(BANCO)
        cursor = conexao.cursor()
        
        sql = "SELECT id, nome, email FROM Clientes WHERE nome LIKE ?"
        cursor.execute(sql, (f"{letra}%",))
        resultados = cursor.fetchall()
        
        print(f"\nClientes que começam com a letra '{letra.upper()}':")
        exibir_resultados(resultados)
        
    finally:
        conexao.close()

def buscar_por_provedor_email(provedor):
    """Consulta avançada: Filtra clientes por provedor (ex: gmail.com)."""
    try:
        conexao = sqlite3.connect(BANCO)
        cursor = conexao.cursor()
        
        sql = "SELECT id, nome, email FROM Clientes WHERE email LIKE ?"
        cursor.execute(sql, (f"%{provedor}",))
        resultados = cursor.fetchall()
        
        print(f"\nClientes usando o provedor '{provedor}':")
        exibir_resultados(resultados)
        
    finally:
        conexao.close()

def exibir_resultados(resultados):
    """Função utilitária apenas para desenhar a tabela de resultados na tela."""
    if not resultados:
        print("Nenhum registro encontrado para este filtro.")
        return
        
    print("-" * 60)
    print(f"{'ID':<5} | {'NOME':<20} | {'EMAIL'}")
    print("-" * 60)
    for c_id, nome, email in resultados:
        print(f"{c_id:<5} | {nome:<20} | {email}")
    print("-" * 60)

if __name__ == "__main__":
    print("=" * 50)
    print("EXECUTANDO CONSULTAS AVANÇADAS E FILTROS")
    print("=" * 50)
    
    buscar_por_inicial("A")

    buscar_por_provedor_email("gmail.com")