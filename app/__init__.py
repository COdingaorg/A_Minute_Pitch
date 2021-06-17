from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config_options
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_wtf import CsrfProtect
from flask_mail import Mail

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
photos = UploadSet('photos', IMAGES)
csrf = CsrfProtect()
mail = Mail()

def create_app(config_name):

  #intializing app
  app = Flask(__name__)

  #creating app configurations
  app.config.from_object(config_options[config_name])

  #Initializing flask extensions
  bootstrap.init_app(app)
  db.init_app(app)
  login_manager.init_app(app)
  csrf.init_app(app)
  mail.init_app(app)
  
  #Registering main Blueprint
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint, url_prefix = '/authenticate')

  #configuring photo uploads
  configure_uploads(app, photos)

  return app