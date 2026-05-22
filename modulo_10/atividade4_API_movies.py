import requests

API_KEY = "31688f183c3c29e0ab9031035c89b197"  
NOME_FILME = "Devoradores de Estrelas"  

URL = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={NOME_FILME}&language=pt-BR"


def buscar_filme():
    try:
        resposta = requests.get(URL, timeout=5)
        resposta.raise_for_status()

        dados = resposta.json()
        resultados = dados.get("results", [])

        if not resultados:
            print(
                f"🔍 Nenhum filme encontrado com o nome '{NOME_FILME}'."
            )
            return

        filme = resultados[0]

        # Filtragem dos dados relevantes
        titulo = filme.get("title", "Sem título")
        titulo_original = filme.get("original_title", "Sem título original")
        sinopse = filme.get("overview", "Sinopse não disponível.")
        data_lancamento = filme.get("release_date", "Data desconhecida")
        nota = filme.get("vote_average", 0.0)

        # Formatando a data de AAAA-MM-DD para DD/MM/AAAA 
        if data_lancamento and "-" in data_lancamento:
            ano, mes, dia = data_lancamento.split("-")
            data_formatada = f"{dia}/{mes}/{ano}"

        else:
            data_formatada = data_lancamento

        # EXIBIÇÃO DOS DADOS ORGANIZADOS
        print("=" * 50)
        print(f"🎬 FILME ENCONTRADO: {titulo.upper()}")
        if titulo.lower() != titulo_original.lower():
            print(f"   (Título Original: {titulo_original})")
        print("=" * 50)

        print(f"📅 Lançamento : {data_formatada}")
        print(f"⭐ Nota (TMDB): {nota}/10")
        print("-" * 50)
        print("📝 SINOPSE:\n")

        import textwrap

        sinopse_formatada = textwrap.fill(sinopse, width=50)
        print(sinopse_formatada)

        print("=" * 50)

    # Tratamento de Erros de Conexão
    except requests.exceptions.Timeout:
        print("⏱ [Erro] O servidor do TMDB demorou muito para responder.")

    except requests.exceptions.ConnectionError:
        print("[Erro] Falha de rede. Verifique sua conexão com a internet.")

    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            print("[Erro 401] Sua Chave de API do TMDB está incorreta.")

        else:
            print(f"[Erro HTTP] Ocorreu um problema: {e.response.status_code}")

    except Exception as erro:
        print(f"💥 Erro inesperado: {erro}")


if __name__ == "__main__":
    buscar_filme()