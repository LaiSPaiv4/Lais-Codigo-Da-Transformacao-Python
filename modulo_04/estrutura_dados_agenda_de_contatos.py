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