print("\n===== Atividade 03 - Sistema Bancário com Validações =====\n")

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_atual, valor_saque):
        self.mensagem = f"Erro: Saldo insuficiente (Saldo: R${saldo_atual:.2f})."
        super().__init__(self.mensagem)

class ContaBancaria:
    def __init__(self, titular, idade, saldo_inicial=0):
        self.titular = titular
        self.idade = idade
        self.saldo = saldo_inicial

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError(self.saldo, valor)
        self.saldo -= valor
        print(f"\nSaque de R${valor:.2f} realizado!")

# FUNÇÕES DE VALIDAÇÃO
def ler_numero_positivo(mensagem):
    # Garante que a entrada seja um número e seja maior que zero.
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print("Valor inválido! Por favor, digite um número maior que zero.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida! Digite apenas números (use ponto para decimais).")

def ler_idade_valida(mensagem):
    while True:
        try:
            idade = int(input(mensagem))
            if 0 <= idade <= 90:
                return idade
            print("Idade irreal! Digite um valor entre 0 e 90.")
        except ValueError:
            print("Erro! A idade deve ser um número inteiro.")

# EXECUÇÃO
def sistema_bancario():
    print("=== Cadastro de Conta ===")
    nome = input("Nome do titular: ").strip()
    # Usando a validação de idade
    idade = ler_idade_valida("Digite sua idade: ")
    # Usando a validação de número positivo para o depósito inicial
    deposito = ler_numero_positivo("Depósito inicial: R$")

    conta = ContaBancaria(nome, idade, deposito)
    print(f"\nConta criada para {conta.titular} ({conta.idade} anos).")

    while True:
        print("\n1. Sacar | 2. Ver Saldo | 3. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            valor_saque = ler_numero_positivo("Quanto deseja sacar? R$")
            try:
                conta.sacar(valor_saque)
            except SaldoInsuficienteError as e:
                print(e)
        elif opcao == "2":
            print(f">> Saldo atual: R${conta.saldo:.2f}")
        elif opcao == "3":
            print("\n>> Saindo do sistema...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    sistema_bancario()