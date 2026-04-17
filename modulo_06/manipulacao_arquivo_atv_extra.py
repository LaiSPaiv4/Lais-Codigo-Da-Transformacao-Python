import shutil
import os
from datetime import datetime

def realizar_backup(pasta_origem, pasta_destino):
    # Verifica se a pasta de origem existe
    if not os.path.exists(pasta_origem):
        print(f"Erro: A pasta de origem '{pasta_origem}' não existe.")
        return

    # Cria um nome único para a pasta de backup usando a data/hora atual
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_backup = f"backup_{timestamp}"
    caminho_final = os.path.join(pasta_destino, nome_backup)

    try:
        shutil.copytree(pasta_origem, caminho_final)
        print(f"Backup concluído com sucesso em: {caminho_final}")
    except Exception as e:
        print(f"Ocorreu um erro durante o backup: {e}")

# Configuração
origem = "meus_documentos"  
destino = "backups_sistema" 

# Cria a pasta de origem para teste se ela não existir
if not os.path.exists(origem):
    os.makedirs(origem)
    with open(f"{origem}/teste.txt", "w") as f: f.write("Arquivo importante!")

realizar_backup(origem, destino)