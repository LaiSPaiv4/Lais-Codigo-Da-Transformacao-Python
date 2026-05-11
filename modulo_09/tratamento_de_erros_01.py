def aula_tratamento_erros():

    print("\n----- Ativdade 01 -----\n")

    try:
        numerador = int(input("Digite o numerador: "))
        denominador = int(input("Digite o denominador: "))
        resultado = numerador / denominador
    except ValueError:
        print("Erro: Digite apenas números inteiros!")
    except ZeroDivisionError:
        print("Erro: Não pode dividir por zero.")
    except Exception as erro:
        print(f"Erro inesperado: {erro}")

    else:
        print(f"Sucesso! Resultado: {resultado}")

    finally:
        print("\n----- Fim da Divisão -----\n")

aula_tratamento_erros()
