print("===== Atividade Extra =====\n")

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_atual, valor_saque):
        self.mensagem = f"Erro: Saldo insuficiente! Saldo: R${saldo_atual:.2f}."
        super().__init__(self.mensagem)

class CredenciaisInvalidasError(Exception):
    def __init__(self):
        self.mensagem = "Erro: Usuário ou senha incorretos!"
        super().__init__(self.mensagem)

# CLASSE BANCÁRIA
class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.saldo = saldo_inicial

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError(self.saldo, valor)
        self.saldo -= valor
        print(f"\nSaque de R${valor:.2f} realizado com sucesso.")

# SISTEMA DE LOGIN
def realizar_login():
    # Simulando um banco de dados: { 'usuario': 'senha' }
    usuarios_cadastrados = {
        "admin": "1234",
        "luke": "maionese"
    }
    
    tentativas = 3
    
    print("=============== ÁREA DE LOGIN ================")
    while tentativas > 0:
        usuario = input("Usuário: ")
        senha = input("Senha: ")
        
        try:
            if usuario in usuarios_cadastrados and usuarios_cadastrados[usuario] == senha:
                print(f"\nLogin bem-sucedido! Bem-vindo(a), {usuario}.")
                return True
            else:
                raise CredenciaisInvalidasError()
        
        except CredenciaisInvalidasError as e:
            tentativas -= 1
            print(f"{e.mensagem} Você tem mais {tentativas} tentativa(s).")
            print("-" * 60)
            
    print("\nSistema bloqueado por excesso de tentativas.")
    return False

# FUNÇÕES DE VALIDAÇÃO
def validar_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida! Digite um número (Ex: 1500.50).")

def main():
    if not realizar_login():
        return 

    print("\n----- Acesso Liberado ao Sistema de Saque -----")
    saldo_inicial = validar_float("Defina seu saldo inicial: R$")
    conta = ContaBancaria("Usuário Logado", saldo_inicial)

    while True:
        print(f"\n>> Saldo atual: R${conta.saldo:.2f}")
        opcao = input("Deseja sacar? (s/n): ").lower()
        
        if opcao == 's':
            valor = validar_float("Valor do saque: R$")
            try:
                conta.sacar(valor)
            except SaldoInsuficienteError as e:
                print(e)
        else:
            print("\n>> Encerrando sessão...")
            break

if __name__ == "__main__":
    main()