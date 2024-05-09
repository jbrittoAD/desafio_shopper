from flask import Flask, request, jsonify
from databaseSchema import db, Cliente, Loja, Produto, RegistroVenda
import pandas as pd
from datetime import datetime
from google.cloud import bigquery
import seaborn as sns
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Inicialize o SQLAlchemy com a aplicação Flask

# Defina o IP e a porta desejados para a aplicação
host = '127.0.0.0'  # IP para escutar em todas as interfaces
port = 5000       # Porta desejada


# Função para criar o banco de dados e suas tabelas
def create_db():
    '''
    Função para criar o banco de dados e suas tabelas.
    '''
    with app.app_context():
        db.create_all()

# Função para processar os dados e gerar visualizações
def generate_visualizations(data):
    # Transformar os dados em DataFrame do Pandas
    df = pd.DataFrame(data)

    # Criar visualização de vendas por produto
    plt.figure(figsize=(10, 6))
    sns.barplot(x='produto_nome', y='vendas', data=df)
    plt.title('Vendas por Produto')
    plt.xlabel('Produto')
    plt.ylabel('Vendas')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Salvar a visualização em um objeto BytesIO
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)

    # Criar CSV com os dados
    csv_data = df.to_csv(index=False)

    return img_bytes, csv_data


@app.route('/')
def index():
    return 'Hello, World!'


# Rota para receber os dados e gerar visualizações
@app.route('/generate_visualizations', methods=['POST'])
def generate_visualizations_route():
    # Obter os dados do corpo da requisição
    data = request.json

    # Chamar a função para gerar as visualizações
    img_bytes, csv_data = generate_visualizations(data)

    # Retornar a imagem e o CSV como resposta
    return jsonify({
        'image': img_bytes.read().decode('latin1'),
        'csv': csv_data
    })

if __name__ == '__main__':
    # Cria o banco de dados se não existir
    create_db()
    # Executa o aplicativo Flask
    app.run(host=host, port=port, debug=True)