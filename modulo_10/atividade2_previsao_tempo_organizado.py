print("----- Atividade 02 -----")

import requests

API_KEY = "086229aae403db8213d5761d35f4ffd4"
CIDADE = "São Paulo"

URL = f"https://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"

try:
    resposta = requests.get(URL)

    if resposta.status_code == 200:
        dados = resposta.json()

        cidade_nome = dados["name"]
        pais = dados["sys"]["country"]

        temp_atual = dados["main"]["temp"]
        temp_max = dados["main"]["temp_max"]
        temp_min = dados["main"]["temp_min"]
        sensacao = dados["main"]["feels_like"]
        condicao = dados["weather"][0]["description"]

        humidade = dados["main"]["humidity"]
        vento = dados["wind"]["speed"]

        # Exibição Organizada 
        print("=" * 40)
        print(f"CONDIÇÕES CLIMÁTICAS: {cidade_nome.upper()} ({pais}) ")
        print("=" * 40)

        print(f"⛅ > Condição atual   : {condicao.capitalize()}")
        print(f"🌡️  > Temperatura      : {temp_atual:.1f}°C")
        print(f"🔥 > Sensação Térmica : {sensacao:.1f}°C")
        print("-" * 40)
        print(f"🔼 > Máxima prevista   : {temp_max:.1f}°C")
        print(f"🔽 > Mínima prevista   : {temp_min:.1f}°C")
        print("-" * 40)
        print(f"💧 > Umidade do Ar     : {humidade}%")
        print(f"🍃 > Velocidade Vento  : {vento} m/s")
        print("-" * 40)

    elif resposta.status_code == 404:
        print("[Erro] Cidade não encontrada. Verifique o nome.")
        
    else:
        print(f"[Erro] Status: {resposta.status_code}")

except Exception as e:
    print(f"Erro de conexão: {e}")