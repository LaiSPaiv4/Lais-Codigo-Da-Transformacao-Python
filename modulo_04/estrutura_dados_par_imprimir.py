print('\n--- Atividade 03 ---')

numeros = [12, 7, 22, 15, 8, 3, 10, 44, 51]

pares = []
impares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n) # Se o resto for 0, vai para os pares
    else:
        impares.append(n) # Caso contrário, vai para os ímpares

# Exibindo os resultados
print(f"\nNúmeros Pares: {pares}")
print(f"Números Ímpares: {impares}\n")

