print("===== Atividade 01 =====\n")

# Criando e Gravando
with open("meu_arquivo.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Olá! Este é um arquivo de texto. Mantenha o foco!\n")
    arquivo.write("Gravando a segunda linha de informação.\n")
    print("Arquivo criado e informações gravadas com sucesso!")

# Lendo as Informações
print("\n---------- Conteúdo do Arquivo ----------\n")
with open("meu_arquivo.txt", "r", encoding="utf-8") as arquivo:
    conteúdo = arquivo.read()
    print(conteúdo)

print("-" * 49)