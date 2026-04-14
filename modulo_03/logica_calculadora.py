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


