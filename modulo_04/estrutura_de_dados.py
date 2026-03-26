'''
Atividades do Módulo 04 sobre Estrutura de Dados
'''

# Atividade 01
print('\n--- Atividade 01 ---\n')

lista_compras = []

while True:
    print('Gestor de Compras')
    print('-' * 20)
    print('1. Adicionar item')
    print('2. Remover item')
    print('3. Visualizar lista')
    print('4. Sair')

    opcao = input('\nEscolha uma opção: ')

    if opcao == '1':
        item = input('Digite o nome do item para adicionar: ')
        lista_compras.append(item)
        print(f"\n '{item}' adicionado com sucesso!\n")

    elif opcao == '2':
        item = input('Digite o nome do item para excluir: ')
        if item in lista_compras:
            lista_compras.remove(item)
            print('>> Item removido!')
        else:
            print('>> Item não encontrado.')

    elif opcao == '3':
        print('\nSua Lista de Compras Atual:')
        print(lista_compras)

    elif opcao == '4':
        print('\nSaindo... Boas compras!')
        break

    else:
        print('\nOpção inválida!')


# Atividade 02
print('\n--- Atividade 02 ---')

aluno = {
    "nome": "Alice",
    "idade": 15,
    "notas": [9.0, 8.0, 8.5],
    "curso": "Web Desing"
}

# Exibindo os dados no console
print('\nInformações Do Aluno')
print('-' * 25)
print(f'Nome: {aluno['nome']}')
print(f"Idade: {aluno['idade']} anos")
print(f"Notas: {aluno['notas']}")
print(f"Curso: {aluno['curso']}")
print('-' * 25)


# Atividade 03
print('\n--- Atividade 03 ---')

numeros = [12, 7, 22, 15, 8, 3, 10, 44, 51]

pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n) # Se o resto for 0, vai para os pares
    else:
        impares.append(n) # Caso contrário, vai para os ímpares

# Exibindo os resultados
print(f"\nNúmeros Pares: {pares}")
print(f"Números Ímpares: {impares}\n")


# Desafio Extra
print('\n--- Desafio Extra ---\n')

agenda = {}

while True:
    
    print("\nAgenda De Contatos")
    print('-' * 25)
    print("1. Adicionar Contato")
    print("2. Remover Contato")
    print("3. Buscar Contato")
    print("4. Listar Todos")
    print("5. Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == '1':
        nome = input("\nDigite o nome do contato: ")
        telefone = input("Digite o telefone: ")
        agenda[nome] = telefone
        print(f"\n>> Contato {nome} salvo!")

    elif opcao == '2':
        nome = input("\nDigite o nome para remover: ")
        if nome in agenda:
            # O .pop remove a chave e retorna o valor (telefone)
            telefone_removido = agenda.pop(nome)
            print(f"Contato {nome} (Tel: {telefone_removido}) foi removido.")
        else:
            print("\nNome não encontrado.\n")

    elif opcao == '3':
        nome = input("\nDigite o nome para buscar: ")
        if nome in agenda:
            print(f">> Telefone de {nome}: {agenda[nome]}")
        else:
            print("\nContato não encontrado.")

    elif opcao == '4':
        print("\n--- MEUS CONTATOS ---\n")
        if not agenda:
            print(">> Sua agenda está vazia.")
        else:
            for nome, telefone in agenda.items():
                print(f"{nome}: {telefone}")

    elif opcao == '5':
        print("\nSaindo da agenda...\n")
        break