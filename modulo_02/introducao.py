''' Atividade de Introdução ao Python '''

import datetime

nome_usuario = input('Digite seu nome: ')
print(f'Olá {nome_usuario}! Seja bem-vindo(a) ao curso de programação em Python, vamos codar!')

#Pega o momento exato agora
agora = datetime.datetime.now()

data_formatada = agora.strftime('%d/%m/%Y %H:%M')
#Exibe a data e hora formatada para o usuário.

print(f'\nHoje é dia: {data_formatada}\n')
