print("\n===== Atividade 01 =====\n")

class Carro:

    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor 

    def buzinar(self):
        print(f'A {self.marca}, do modelo {self.modelo}, da cor {self.cor}. fez: Bip Bip!')

meu_carro = Carro('Honda', 'Civic', 'preto')

carro_do_cliente = Carro('Volkswagen', 'T-Cross', 'cinza platinum')

meu_carro.buzinar()
carro_do_cliente.buzinar()