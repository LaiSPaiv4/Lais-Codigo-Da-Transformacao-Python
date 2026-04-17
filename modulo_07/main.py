import utilidades

print("\n===== Atividade 01 =====\n")

num1 = 20
num2 = 4

resultado_soma = utilidades.somar(num1, num2)
print(f"O resultado da soma entre {num1} e {num2} é: {resultado_soma}")

resultado_sub = utilidades.subtrair(num1, num2)
print(f"O resultado da subtração entre {num1} e {num2} é: {resultado_sub}")

resultado_pot = utilidades.potencia(num1, 2)
print(f"O número {num1} elevado a 2 é: {resultado_pot}\n")