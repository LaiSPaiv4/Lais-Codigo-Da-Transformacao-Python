
print("\n===== Atividade 02 - Programa Bancário =====\n")

class SaldoInsuficienteError(Exception):
    def __init__(self, saldo_atual, valor_saque):
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque
        self.mensagem = f"Erro: Saldo insuficiente. Tentativa de sacar R${valor_saque:.2f}, mas seu saldo é de R${saldo_atual:.2f}."
        super().__init__(self.mensagem)

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def sacar(self, valor):
        print(f"\n--- Tentativa de saque: R${valor:.2f} ---")
        if valor > self.saldo:
            raise SaldoInsuficienteError(self.saldo, valor)
        
        self.saldo -= valor
        print(f"Saque realizado com sucesso! Novo saldo: R${self.saldo:.2f}")
        
# Simulção do Sistema
def executar_simulacao():
        minha_conta = ContaBancaria("Eliza", 500.00)
        print(f"Bem-vindo(a), {minha_conta.titular}! |Saldo inicial: R${minha_conta.saldo:.2f}|")

        try:
            # Primeira tentatiiva: Saque dentro do limite
            minha_conta.sacar(200.00)

            # Segunda tentativa: Saque que causará o erro
            minha_conta.sacar(400.00)
        
        except SaldoInsuficienteError as e:
             # Captura apenas o erro especifico que criamos
             print(e)
        except Exception as e:
             # Captura qualquer outro erro inesperado
             print(f"Ocorre um erro inesperado: {e}")
        finally:
             print("\n>> Operação finalizada.")
    
if __name__ == "__main__":
    executar_simulacao()