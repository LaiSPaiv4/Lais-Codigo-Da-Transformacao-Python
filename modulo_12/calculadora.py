# Função isolada (Atividade 1)
def somar_numeros(a, b):
    return a + b


# Classe Calculadora (Atividades 2 e 3)
class Calculadora:

    def somar(self, a, b):
        return a + b

    def dividir(self, a, b):
        if b == 0:
            # Lança o erro esperado para a Atividade 3
            raise ValueError("Não é possível dividir por zero.")
        return a / b