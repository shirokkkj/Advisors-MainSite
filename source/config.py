from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy


MASTER_PASSWORD = 'masterloginpassword'
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = ''
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

    
    
    
    
    # Aqui em cima, nos [app.config], configurei tudo o que foi necessário pro código rodar. A Secret Key, pro WTForms poder funcionar, já que ele exige que uma chave secreta seja passado. ( Eu usei a biblioteca secrets pra gerar essa chave secreta)
    # Logo após, configurei o SQLALCHEMY_DATABASE_URI, no caso, estou passando qual Banco de dados devo me conectar. Passei o [...] com senha, host e porta assim, conectando-o e usufruindo da ferramenta.

    db.init_app(app) # Iniciei o banco de dados, tendo passado a variável [db] lá em cima, porque se não iria gerar uma confusão danada...

    from views.table import table_route
    from views.form_products import form_register
    from views.navbar import nav_route
    from views.selected_data import dates_route
    from views.vendas import sealler_route
    from routes import config_routes
    from views.errors import errors
    
    # Importei todas as rotas e as configurei como BluePrints, e, logo depois, configurei as rotas tendo importado a função do arquivo [routes] pra manter a modularização organizada e sem aquele problema de importação circular.

    app.register_blueprint(form_register)
    app.register_blueprint(nav_route)
    app.register_blueprint(table_route)
    app.register_blueprint(dates_route)
    app.register_blueprint(sealler_route)
    app.register_blueprint(errors)
    config_routes('masterloginpassword', app)
    
    
    with app.app_context():
        db.create_all()
        print('condition')

    return app
