class Carro:

    def __init__(self, marca, cor):
        self.marca = marca
        self.cor = cor 

    def buzinar(self):
        print(f'O {self.marca} da cor {self.cor} fez: Bip Bip!')

meu_carro = Carro('Civic', 'preto')

carro_do_cliente = Carro('Honda', 'preto')

meu_carro.buzinar()
carro_do_cliente.buzinar()