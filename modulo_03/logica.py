'''
Atividades do Módulo 3 sobre Lógica da Programação
'''

# ATIVIDADE 01
print('\n--- ATIVIDADE 01 ---\n')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2

print(f'\n--- Resultados para {n1} e {n2} ---')
print('-' * 30)
print(f'Soma: {soma}')
print(f'Diferença: {subtracao}')
print(f'Multiplicação: {multiplicacao}')

if n2 != 0:
    divisao = n1 / n2
    print(f'Divisão: {divisao}')
    print('-' * 30)

else:
    print('Divisão: Não é possivel dividir por zer!')


# ATIVIDADE 02
print('\n--- ATIVIDADE 02 ---\n')

v1 = int(input('Digite um valor: '))
v2 = int(input('Digite outro valor: '))

if v1 > v2:
    print(f'O maior número é: {v1}')

elif v2 > v1:
    print(f'O maior número é: {v2}')

else:
    print('Os dois números são iguais.')


# ATIVIDADE 03
print('\n--- ATIVIDADE 03 ---\n')

idade = int(input('Digite sua idade: '))

if idade <= 11: 
    print('Você é uma criança. (👶)')

elif idade <= 17:
    print('Você é um adolescente. (🧑)')

elif idade <= 59:
    print('Você é um adulto. (🧔)')

else:
    print('Você é um idoso. (🧑‍🦳)')


# ATIVIDADE EXTRA
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