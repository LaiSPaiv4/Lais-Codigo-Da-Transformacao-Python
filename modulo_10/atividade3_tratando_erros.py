print("----- Atividade 03 -----")

import requests

API_KEY = "086229aae403db8213d5761d35f4ffd4"
CIDADE = "Sao Paulo"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CIDADE}&appid={API_KEY}&units=metric&lang=pt_br"

try:
    resposta = requests.get(URL, timeout=5)
    
    resposta.raise_for_status()

    dados = resposta.json()

    cidade_nome = dados["name"]
    temp_atual = dados["main"]["temp"]
    condicao = dados["weather"][0]["description"]

    print("=" * 40)
    print(f"🌤️  > Clima em {cidade_nome}: {condicao.capitalize()}")
    print(f"🌡️  > Temperatura: {temp_atual:.1f}°C")
    print("=" * 40)

except requests.exceptions.Timeout:
    print(" ⏱ [Erro] A conexão demorou muito para responder. Verifique sua internet ou tente mais tarde.")

except requests.exceptions.ConnectionError:
    print("[Erro] Falha na conexão de rede. Certifique-se de que você está conectado à internet.")

except requests.exceptions.HTTPError as erro_http:
    status_code = erro_http.response.status_code
    if status_code == 404:
        print(f"[Erro {status_code}] Cidade '{CIDADE}' não encontrada.")

    elif status_code == 401:
        print(f"[Erro {status_code}] Chave de API inválida ou não ativada.")
        
    else:
        print(f"[Erro HTTP {status_code}] O servidor retornou um erro.")

except ValueError: 
    print("[Erro] A API enviou dados em um formato inválido (não foi possível ler o JSON).")

# 5. Uma "rede de segurança" para qualquer outro erro inesperado que não mapeamos acima
except requests.exceptions.RequestException as erro_geral:
    print(f"💥 Ocorreu um erro inesperado na requisição: {erro_geral}")