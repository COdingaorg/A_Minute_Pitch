from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config_options

db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name):

  #intializing app
  app = Flask(__name__)

  #creating app configurations
  app.config.from_object(config_options[config_name])

  #Initializing flask extensions
  bootstrap.init_app(app)
  db.init_app(app)
  
  #Registering main Blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')

  return app