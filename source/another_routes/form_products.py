from flask import Blueprint, render_template, request, redirect, url_for
from form.forms import User_Register
from configs.sqlalchemy import Users, db

form_register = Blueprint('register', __name__)

@form_register.route('/register', methods=['GET', 'POST'])
def register():
    form = User_Register()
    print(f"Request method: {request.method}")

    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = Users(name=form.name.data, password=form.password.data)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('register'))
        else:
            print("Form validation failed")

    return render_template('add_clients.html', form=form)


# Usando uma BluePrint, registei uma rota chamada /register, passando os métodos [GET, POST], assim, podendo renderizar o conteúdo da página e ao mesmo tempo, recebendo os dados com o [form.validate_on_submit] ( validator do wtforms) e com o método POST. Registrei o usuário no banco de dados e redirecionei de novo pra rota de register, é uma baita de uma gambiarra, mas que pretendo melhorar depois.