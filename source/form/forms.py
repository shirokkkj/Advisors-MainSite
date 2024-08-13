from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FloatField, DateField
from wtforms.validators import DataRequired


class Login(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    


class User_Register(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_register = SubmitField('Registrar')
    
class Edit_User(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit_edit = SubmitField('Editar')
    
class Vendas(FlaskForm):
   investment = FloatField('Investment', validators=[DataRequired()])
   date = DateField('Date of Investment. 00/00', validators=[DataRequired()])
   submit_vendas = SubmitField('Create Investment')

    