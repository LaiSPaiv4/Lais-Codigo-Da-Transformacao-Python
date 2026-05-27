import pytest
# Importamos o app Flask do nosso arquivo anterior
from app_api import app

@pytest.fixture
def client():
    """Configura o cliente de testes do Flask automaticamente."""
    with app.test_client() as client:
        yield client

def test_rota_status_deve_retornar_200_e_json_correto(client):
    """Testa se a rota /api/status responde corretamente."""
    # Simula uma requisição GET na rota da API
    resposta = client.get('/api/status')
    
    # Converte a resposta recebida para um dicionário Python
    dados = resposta.get_json()
    
    # Validações (Asserts)
    assert resposta.status_code == 200
    assert dados["status"] == "operando"
    assert "mensagem" in dados