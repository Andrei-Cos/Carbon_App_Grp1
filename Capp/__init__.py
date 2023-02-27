from flask import Flask

application = Flask(__name__)

from Capp.home.routes import home
from Capp.methodology.routes import methodology
from Capp.carbon_app.routes import carbon_app
from Capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(users)