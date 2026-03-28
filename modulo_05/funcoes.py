''' 
Atividade Módulo 05 sobre Funções em Python.
'''

print('\n--- Atividade 01 ---\n')
print('==== Mensagem de Boas-Vindas ====\n')

def saudacao(nome):
    print(f'Olá, {nome}! Seja muito bem-vindo(a) ao mundo da programação com Python.')

saudacao("Marie")


print('\n--- Atividade 02 ---\n')

def calcular_media(notas_lista):
    media_final = sum(notas_lista) / len(notas_lista)
    if media_final >= 7:
        status = "Aprovado"
    else:
        status = "Reprovado" 

    return media_final, status

# Dados de entrada
notas_bimestre = [8.5, 7.0, 9.5, 6.0]

# Processamento
media, status = calcular_media(notas_bimestre)

print("==== BOLETIM DE NOTAS ====\n")
print(f"Notas: {notas_bimestre}")
print(f"Média Final: {media:.2f} - Status: {status}")


print('\n--- Atividade 03 ---\n')

def maior_menor(lista_numeros):
    maior = max(lista_numeros)
    menor = min(lista_numeros)
    
    return maior, menor

numeros = [15, 8, 43, 2, 27, 5]

v_maior, v_menor = maior_menor(numeros)

print("==== ANÁLISE DE VALORES ====\n")
print(f'Lista analisada: {numeros}')
print(f'Maior valor: {v_maior}')
print(f'Menor valor: {v_menor}')


print('\n--- Atividade Extra ---\n')

# Dicionário
usuarios_cadastrados = {
    "admin": "1234",
    "aluno_python": "nev258",
    "professor": "computador26"
}

def validar_login(usuario, senha):
    # Verifica se o usuário existe no dicionário e se a senha coincide
    if usuario in usuarios_cadastrados and usuarios_cadastrados[usuario] == senha:
        return True
    else:
        return False

# Simulçao de digitação
user_input = "aluno_python"
pass_input = "nev258"

acesso_concedido = validar_login(user_input, pass_input)

print("==== SISTEMA DE LOGIN ====\n")
if acesso_concedido:
    print(f'Bem-vindo, {user_input}! Acesso LIBERADO ')
else:
    print('Erro: Usuário ou senha incorretos. Acesso NEGADO\n')