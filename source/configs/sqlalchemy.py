from config import db
import datetime

# Aqui é toda a criaão e configuração do banco de dados usando SQLAlchemy. Através deste arquivo, as colunas dentro do banco de dados usado é criado com os parâmetros passados, nesse cado, o

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.now())
    
    def __repr__(self):
        return f'{self.name}, {self.password}, {self.date}'
    
    
class Investments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_investment = db.Column(db.String(150), unique=False, nullable=False)
    investment = db.Column(db.Float, nullable=False, unique=False)
    date = db.Column(db.DateTime)