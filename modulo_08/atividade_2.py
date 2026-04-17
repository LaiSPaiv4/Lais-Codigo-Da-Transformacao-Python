print("\n===== Atividade 02 =====\n")

class Carro:
    
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano

    def exibir_info(self):
        print(f"Veículo: {self.modelo} | Ano: {self.ano}")


class CarroEletrico(Carro):
    def __init__(self, modelo, ano, autonomia_bateria):
   
        super().__init__(modelo, ano)
      
        self.autonomia_bateria = autonomia_bateria

    def exibir_info_eletrico(self):
    
        print(f"Veículo Elétrico: {self.modelo} ({self.ano})")
        print(f"Autonomia: {self.autonomia_bateria}km")

meu_tesla = CarroEletrico("BYD Seal", 2024, 520)

meu_tesla.exibir_info_eletrico()