print('\n--- Desafio Extra ---\n')

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

while True:
     
     print('\n--- Menu de Operações ---')
     print('-' * 25)
     print('1. Soma')
     print('2. Subtração')
     print('3. Sair')

     escolha = input('\nEscolha uma opção: ')

     if escolha == '1':
         soma = num1 + num2
         print(f'\nO resultado da soma é {soma}')

     elif escolha == '2':
         subtracao = num1 - num2
         print(f'\nO resultado da subtração é {subtracao}')
     
     elif escolha == '3': 
        print('\nVocê encerrou o programa. Volte sempre!')
        break

     else: 
        print('\nOpção inválida! Tente novamente.')