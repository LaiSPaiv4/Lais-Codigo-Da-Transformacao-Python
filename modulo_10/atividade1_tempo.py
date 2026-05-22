print("\n----- Atividade 01 -----")

import requests

API_KEY = "086229aae403db8213d5761d35f4ffd4"
CIDADE = "São Paulo"

URL = f"https://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"

try:
    resposta = requests.get(URL)

    if resposta.status_code == 200:
        dados = resposta.json()

        temperatura = dados["main"]["temp"]
        condicao = dados["weather"][0]["description"]
        humidade = dados["main"]["humidity"]

        print(f"\n---- Previsão do Tempo para: {CIDADE} ----\n")
        print(f"Temperatura atual: {temperatura}°C")
        print(f"Condição climática: {condicao.capitalize()}")
        print(f"Umidadde do ar: {humidade}%")

    elif resposta.status_code == 401:
        print("Erro: Chave de APT inválida ou ainda não ativada pelo OpenWeather.")

    elif resposta.status_code == 404:
        print("Erro: Cidade não encontrada. Verifique a ortografia.")

    else: 
        print(f"Houve um erro inesperado. Código do status: {resposta.status_code}")

except Exception as erro:
    print(f"Ocorreu uma falha na conexão: {erro}")