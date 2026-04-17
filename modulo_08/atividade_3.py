print("\n===== Atividade 03 =====\n")

class Celular:
    def __init__(self, modelo, memoria, cor):
        self.modelo = modelo
        self.memoria = memoria
        self.cor = cor
        self.ligado = False

    def __str__(self):
        status = "Ligado" if self.ligado else "Desligado"
        return f"{self.modelo} ({self.cor}) - {self.memoria}GB [Status: {status}]"

    def ligar_desligar(self):
        self.ligado = not self.ligado
        estado = "ligado" if self.ligado else "desligado"
        print(f"O {self.modelo} foi {estado}!\n")


celular1 = Celular("iPhone 15", 128, "Titânio")
celular2 = Celular("Galaxy S24", 256, "Preto")

print(celular1)
print(celular2)

celular1.ligar_desligar()
print(celular1)