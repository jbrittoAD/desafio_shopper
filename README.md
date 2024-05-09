---

# README

## Projeto Flask para Geração de Visualizações

Este é um projeto Flask simples que demonstra como gerar visualizações a partir de dados enviados via solicitação POST. Ele inclui um endpoint `/generate_visualizations` que recebe dados JSON, gera uma visualização de barras usando seaborn e retorna a visualização como uma imagem PNG, juntamente com os dados originais em formato CSV.

## Instalação

Para executar este projeto localmente, siga estas etapas:

1. Clone este repositório para o seu ambiente local:

```
git clone https://github.com/seu-usuario/nome-do-repositorio.git
```

2. Navegue até o diretório do projeto:

```
cd nome-do-repositorio
```

3. Instale as dependências usando pip:

```
pip install -r requirements.txt
```

## Utilização

Para executar o aplicativo Flask, você pode simplesmente executar o arquivo `app.py`:

```
python app.py
```

Isso iniciará o servidor Flask localmente. Você poderá acessar o aplicativo Flask em `http://127.0.0.1:5000/`.

### Gerar Visualizações

Para gerar visualizações, envie uma solicitação POST para a rota `/generate_visualizations` com dados JSON no corpo da solicitação. Por exemplo:

```python
import requests
import json

data = [
    {"produto_nome": "Produto A", "vendas": 10},
    {"produto_nome": "Produto B", "vendas": 20}
]

response = requests.post('http://127.0.0.1:5000/generate_visualizations', json=data)
result = response.json()

# O resultado inclui a imagem e os dados em formato CSV
print("Imagem:", result['image'])
print("CSV:", result['csv'])
```

## Testes

Este projeto inclui testes automatizados escritos com pytest para garantir que as funcionalidades principais estejam funcionando corretamente. Para executar os testes, use o pytest:

```
pytest
```

Os testes incluem:

- Teste para a rota principal (`/`) para garantir que ela retorne uma mensagem "Hello, World!".
- Teste para a rota de geração de visualizações (`/generate_visualizations`) para garantir que ela responda corretamente a uma solicitação POST e retorne uma visualização e dados em formato CSV.

## Interpretação dos Testes

Durante a execução dos testes, você verá a saída do pytest no terminal. Se todos os testes passarem, você verá mensagens indicando que os testes foram bem-sucedidos. Se algum teste falhar, você verá uma mensagem de falha específica para indicar qual teste falhou e qual foi o problema encontrado.

---
