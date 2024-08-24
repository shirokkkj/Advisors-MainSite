from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField
from wtforms.fields import DateField
from wtforms.validators import DataRequired



# Aqui é bem simples. Eu configurei todos os formulários do site nesse arquivo, ou seja, o formulário de Login, o de Registrar Usuários e o de Vendas. Usei WTForms

class Login(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    


class User_Register(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_register = SubmitField('Registrar')
    
    
class Vendas(FlaskForm):
    name_investment = StringField('Name of Investment', validators=[DataRequired()])
    investment = FloatField('Investment', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d')
    submit_vendas = SubmitField('Create Investment')

    