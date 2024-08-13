from flask import Flask
from flask_sqlalchemy import SQLAlchemy

MASTER_PASSWORD = 'masterloginpassword'
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '9efaec900d476ff1f3a2384a4b66d1ae'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:shirostrongpassword@127.0.0.1:3306/database_advisors'
    
    # Aqui em cima, nos [app.config], configurei tudo o que foi necessário pro código rodar. A Secret Key, pro WTForms poder funcionar, já que ele exige que uma chave secreta seja passado. ( Eu usei a biblioteca secrets pra gerar essa chave secreta)
    # Logo após, configurei o SQLALCHEMY_DATABASE_URI, no caso, estou passando qual Banco de dados devo me conectar. Passei o [...] com senha, host e porta assim, conectando-o e usufruindo da ferramenta.

    db.init_app(app) # Iniciei o banco de dados, tendo passado a variável [db] lá em cima, porque se não iria gerar uma confusão danada...

    from another_routes.table import table_route
    from another_routes.form_products import form_register
    from another_routes.navbar import nav_route
    from another_routes.selected_data import dates_route
    from another_routes.vendas import sealler_route
    from routes import config_routes
    
    # Importei todas as rotas e as configurei como BluePrints, e, logo depois, configurei as rotas tendo importado a função do arquivo [routes] pra manter a modularização organizada e sem aquele problema de importação circular.

    app.register_blueprint(form_register)
    app.register_blueprint(nav_route)
    app.register_blueprint(table_route)
    app.register_blueprint(dates_route)
    app.register_blueprint(sealler_route)

    config_routes('masterloginpassword', app)
    with app.app_context():
        db.create_all()

    return app
