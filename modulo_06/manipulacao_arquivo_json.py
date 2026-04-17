import json

print("===== Atividade 02 =====\n")

clientes = {
    "1": {"nome": "Ana Silva", "email": "ana@email.com", "premium": True},
    "2": {"nome": "Bruno Costa", "email": "bruno@email.com", "premium": False},
    "3": {"nome": "Carla Dias", "email": "carla@email.com", "premium": True}
}

with open("clientes.json", "w", encoding="utf-8") as arquivo:
    json.dump(clientes, arquivo, indent=4, ensure_ascii=False)
    print("Dicionário de clientes salvo com sucesso!")

print("\n-------- Carregando Dados do JSON --------\n")
with open("clientes.json", "r", encoding="utf-8") as arquivo:
    dados_carregados = json.load(arquivo)

    for id_cliente, info in dados_carregados.items():
        status = "VIP" if info['premium'] else "Normal"
        print(f"ID: {id_cliente} | Nome: {info['nome']} | Status: {status}")

print("-" * 42)