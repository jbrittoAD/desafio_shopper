import pytest
import json
from app import app, db

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_generate_visualizations_route(client):
    # Dados de exemplo para enviar na solicitação POST
    data = [
        {"produto_nome": "Produto A", "vendas": 10},
        {"produto_nome": "Produto B", "vendas": 20}
    ]

    # Envia uma solicitação POST para a rota /generate_visualizations com os dados de exemplo
    response = client.post('/generate_visualizations', json=data)

    print("Response Status Code:", response.status_code)
    print("Response Data:", response.data)

    # Verifica se a resposta tem status 200
    assert response.status_code == 200
    
    # Verifica se a resposta contém a chave 'image'
    assert 'image' in json.loads(response.data)
    
    # Verifica se a resposta contém a chave 'csv'
    assert 'csv' in json.loads(response.data)
