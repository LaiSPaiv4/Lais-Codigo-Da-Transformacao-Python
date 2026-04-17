import csv
import os

print("\n===== Atividade 03 =====")

def adicionar_nota(nome_arquivo):
    nome = input("\nDigite o nome do aluno: ")
    materia = input("Digite a matéria: ")
    nota = input("Digite a nota: ")
    
    with open(nome_arquivo, 'a', newline='', encoding='utf-8') as arquivo:
        escritor = csv.writer(arquivo)
        
        if os.stat(nome_arquivo).st_size == 0:
            escritor.writerow(["Nome", "Materia", "Nota"])

        escritor.writerow([nome, materia, nota])
    print("-" * 23)
    print("Nota salva com sucesso!")
    print("-" * 23)

def exibir_notas(nome_arquivo):
    print("\n---------- Notas dos Alunos ----------\n")
    if not os.path.exists(nome_arquivo):
        print("O arquivo ainda não existe. Adicione uma nota primeiro.")
        return
    
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        for i, linha in enumerate(leitor):
            if i == 0:
                print("-" * 41)
                print(f"{linha[0]:<15} | {linha[1]:<15} | {linha[2]}")
                print("-" * 41)
            else:
                print(f"{linha[0]:<15} | {linha[1]:<15} | {linha[2]}")

# Execução do Programa
ARQUIVO = "notas_alunos.csv"

while True:
    opcao = input("\n1. Adicionar Nota\n2. Ver Notas\n3. Sair\n \nEscolha: ")
    if opcao == '1':
        adicionar_nota(ARQUIVO)
    elif opcao == '2':
        exibir_notas(ARQUIVO)
    elif opcao == '3':
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
