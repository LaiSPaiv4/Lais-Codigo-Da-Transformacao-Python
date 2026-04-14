'''
Atividades do Módulo 04 sobre Estrutura de Dados
'''

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
