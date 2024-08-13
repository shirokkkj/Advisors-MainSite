from flask import Blueprint, render_template, request

dates_route = Blueprint('dates', __name__)

@dates_route.route('/date_selected')
def date():
    data = request.json
    print(data['date'])
    return render_template('home.html')


# Essa rota aqui é simplesmente pra renderizar a sidebar.