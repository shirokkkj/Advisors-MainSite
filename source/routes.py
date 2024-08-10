from flask import render_template, redirect, request, flash, make_response, url_for
from form.forms import Login
from another_routes.table import table_route
from another_routes.form_products import form_register
from another_routes.navbar import nav_route
from configs.sqlalchemy import Users

def config_routes(MASTER_PASSWORD, app):
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = Login()
        cookie_name = request.cookies.get('name')
        cookie_password = request.cookies.get('password')
        
        if not cookie_name and not cookie_password:    
            if request.method == 'POST':
                    if form.validate_on_submit() and form.password.data == MASTER_PASSWORD:
                        cookie = make_response(redirect(url_for('register')))
                        cookie.set_cookie('name', form.name.data)
                        cookie.set_cookie('password', form.password.data)
                        return cookie      
                    else:
                        try:
                            user = Users.query.get(Users.name == form.name.data)         
                            cookie = make_response(redirect(url_for('home')))
                            cookie.set_cookie('name', form.name.data)
                            cookie.set_cookie('password', form.password.data)
                            return cookie     
                        except:
                            flash('Esse usuário não existe.', 'danger')
        else:
            return redirect(url_for('home'))
        
        return render_template('login.html', form=form)


    @app.route('/home', methods=['GET', 'POST'])
    def home():
        v = [0, 35.32, -20, -40, -25, -30, -40, -65]
        dates = [date for date in range(2000, 2024)]
        days = [day for day in range(1, 31)]
        data = {
            'labels': ['05/09', '06/09', '06/09', '07/09', '08/09', '09/09', '10/09'],
            'values': [i for i in v]
        }
        cookie = request.cookies.get('name')
        cookie_password = request.cookies.get('password')
        resultado = sum(v)
        
        user_id = Users.query.get(cookie)
        
        if not cookie and not cookie_password:
            return redirect(url_for('login'))
        return render_template('home.html', data=data, cookie_name=cookie, user_id=user_id, cookie_password=cookie_password, resultado=resultado, dates=dates, days=days)

    @app.route('/cadaster', methods=['GET', 'POST'])
    def register():
        cookie = request.cookies.get('name')
        cookie_password = request.cookies.get('password')
        
        if not cookie and not cookie_password:
            return redirect(url_for('login'))
        
        if cookie_password != MASTER_PASSWORD:
            return redirect(url_for('home'))

        return render_template('cadastrar.html')
    
    