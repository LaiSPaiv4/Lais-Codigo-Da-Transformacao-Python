print('\n--- Atividade 02 ---\n')

def calcular_media(notas_lista):
    media_final = sum(notas_lista) / len(notas_lista)
    if media_final >= 7:
        status = "Aprovado"
    else:
        status = "Reprovado" 

    return media_final, status

# Dados de entrada
notas_bimestre = [8.5, 7.0, 9.5, 6.0]

# Processamento
media, status = calcular_media(notas_bimestre)

print("==== BOLETIM DE NOTAS ====\n")
print(f"Notas: {notas_bimestre}")
print(f"Média Final: {media:.2f} - Status: {status}")

