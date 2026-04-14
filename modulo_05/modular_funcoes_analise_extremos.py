print('\n--- Atividade 03 ---\n')

def maior_menor(lista_numeros):
    maior = max(lista_numeros)
    menor = min(lista_numeros)
    
    return maior, menor

numeros = [15, 8, 43, 2, 27, 5]

v_maior, v_menor = maior_menor(numeros)

print("==== ANÁLISE DE VALORES ====\n")
print(f'Lista analisada: {numeros}')
print(f'Maior valor: {v_maior}')
print(f'Menor valor: {v_menor}')

