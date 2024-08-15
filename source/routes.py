from flask import render_template, redirect, request, flash, make_response, url_for
from form.forms import Login
from another_routes.table import table_route
from another_routes.form_products import form_register
from another_routes.navbar import nav_route
from configs.sqlalchemy import Users, Investments
import datetime


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
        
        converted_dates = None
        query_values = None
        passed_values = None
        investment_values = ''
        correct_data = ''
        data = ''
        
        if request.method == 'POST':
            data = request.form.get(key='date')
            correct_data = data.split(', ')  
            
        
        if data and correct_data:
            converted_dates = [datetime.datetime.strptime(data, '%m/%d/%Y').strftime('%Y-%m-%d') for data in correct_data]
            
        if converted_dates:
            query_values = Investments.query.filter(Investments.date.in_(converted_dates)).all()
            passed_values = [value for value in query_values]
        
            investment_values = [values.investment for values in passed_values]
            print(investment_values)
            
        dates = {
            'labels': correct_data if correct_data else '00/00',
            'values': investment_values if investment_values else 00
        }
        
        
        
        
        cookie = request.cookies.get('name')
        cookie_password = request.cookies.get('password')
        result_of_tratament = sum(investment_values) if investment_values else ''
        result = f'{result_of_tratament:.2f}' if result_of_tratament else ''
        
        user_id = Users.query.get(cookie)
        
        if not cookie and not cookie_password:
            return redirect(url_for('login'))
        return render_template('home.html', data=dates, cookie_name=cookie, user_id=user_id, cookie_password=cookie_password, resultado=result)

    @app.route('/cadaster', methods=['GET', 'POST'])
    def register():
        cookie = request.cookies.get('name')
        cookie_password = request.cookies.get('password')
        
        if not cookie and not cookie_password:
            return redirect(url_for('login'))
        
        if cookie_password != MASTER_PASSWORD:
            return redirect(url_for('home'))

        return render_template('cadastrar.html')
    
    @app.route('/investments_products')
    def investments():
        return render_template('register_investments.html')