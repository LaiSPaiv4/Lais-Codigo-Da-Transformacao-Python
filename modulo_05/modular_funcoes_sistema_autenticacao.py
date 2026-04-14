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