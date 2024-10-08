from flask import Blueprint, render_template, request, redirect, url_for
from configs.sqlalchemy import Users, db
from form.forms import User_Register

table_route = Blueprint('table', __name__)

@table_route.route('/table', methods=['GET', 'DELETE', 'POST'])
def table():
    users = Users.query.all()
    return render_template('table_products.html', users=users)

@table_route.route('/<int:user_id>/delete', methods=['DELETE'])
def delete_user(user_id):
    user = Users.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return Users()

# @table_route.route('/table/<int:user_id>/edit', methods=['GET'])

    
@table_route.route('/<int:user_id>/update', methods=['GET'])
def update_user(user_id):
        user = Users.query.get(user_id)
        form = User_Register(obj=user)
    
        if form.validate_on_submit():
            form.populate_obj(user)
        return render_template('add_clients.html', user=user, form=form)
    
@table_route.route('/<int:user_id>/update_user', methods=['GET', 'POST'])
def update_user_id(user_id):
    user = Users.query.get(user_id)
    form = User_Register()
    
    if form.validate_on_submit():
        user.name = form.name.data
        user.password = form.password.data  
        db.session.commit()
        return redirect(url_for('register'))
    return render_template('add_clients.html', user=user, form=form)
