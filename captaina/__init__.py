from flask import Flask
from flask_bcrypt import Bcrypt
import pymodm as modm
from flask_login import LoginManager
from flask_wtf import CSRFProtect
fbcrypt = Bcrypt()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app(**config_overrides):
    app = Flask('captaina', instance_relative_config=True)

    app.config.from_object('config')
    app.config.from_pyfile('config.py')
    app.config.update(config_overrides)

    csrf.init_app(app) 
    fbcrypt.init_app(app)
    login_manager.init_app(app)
    from .utils import handle_needs_login
    login_manager.unauthorized_handler(handle_needs_login)
    modm.connect(app.config['MONGO_DATABASE_URI'])
    from .views import register_blueprints
    register_blueprints(app)
    from .cli import register_cli
    register_cli(app)
    return app

