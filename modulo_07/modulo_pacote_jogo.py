import random
import math

def jogar():
    print("==================================")
    print("   BEM-VINDO AO ADIVINHA-PYTHON  ")
    print("==================================")
    
    # Gera um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False
    
    print("Tente adivinhar o número entre 1 e 100!")

    while not acertou:
        chute = int(input("\nQual o seu chute? "))
        tentativas += 1
        
        distancia = math.fabs(numero_secreto - chute)
        
        if chute == numero_secreto:
            print(f"PARABÉNS! Você acertou em {tentativas} tentativas.")
            acertou = True
        elif chute < numero_secreto:
            print("O número secreto é MAIOR.")
        else:
            print("O número secreto é MENOR.")
            
        # Dica extra usando a distância calculada
        if not acertou and distancia <= 5:
            print("DICA: Você está MUITO quente! (Menos de 5 de distância)")

jogar()