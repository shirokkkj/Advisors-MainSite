from config import db
import datetime

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.Integer, unique=True, nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.now())
    
    def __repr__(self):
        return f'{self.name}, {self.password}, {self.date}'
    
    
class Investments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    investment = db.Column(db.Float, nullable=False, unique=False)
    date = db.Column(db.DateTime)