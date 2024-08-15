from flask import Blueprint, render_template, request, flash, redirect, url_for
from form.forms import Vendas
from configs.sqlalchemy import Investments, db

sealler_route = Blueprint('sealler', __name__)

@sealler_route.route('/investments', methods=['GET', 'POST'])
def seal():
    print(request.method)
    form = Vendas()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            new_investment = Investments(investment=form.investment.data, date=form.date.data)
            db.session.add(new_investment)
            db.session.commit()
            return redirect(url_for('investments'))
        else:
            flash('Algo deu errado!')
            return redirect(url_for('investments'))
    return render_template('form_vendas.html', form=form)