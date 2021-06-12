from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):

  #intializing app
  app = Flask(__name__)

  #creating app configurations
  app.config.from_object(config_options[config_name])

  #Initializing flask extensions
  bootstrap.init_app(app)  

  from .main import views, forms, errors

  return app