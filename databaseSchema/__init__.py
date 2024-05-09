from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    endereco = db.Column(db.String(200))

class Loja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    proprietario_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    proprietario = db.relationship('Cliente', backref=db.backref('lojas', lazy=True))

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.Text)
    preco = db.Column(db.Float)
    estoque = db.Column(db.Integer)
    loja_id = db.Column(db.Integer, db.ForeignKey('loja.id'))
    loja = db.relationship('Loja', backref=db.backref('produtos', lazy=True))

class RegistroVenda(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produto.id'))
    produto = db.relationship('Produto', backref=db.backref('registros_venda', lazy=True))
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    cliente = db.relationship('Cliente', backref=db.backref('compras', lazy=True))
    quantidade = db.Column(db.Integer)
    data_venda = db.Column(db.DateTime)
