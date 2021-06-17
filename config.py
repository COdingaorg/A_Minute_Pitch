import os
class Config:
  '''
  General configurations for the application
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/pitch_minute'
  SECRET_KEY = os.environ.get('SECRET_KEY')
  UPLOADED_PHOTOS_DEST = 'app/static/photos'

  #  email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
  '''
  Configurations for production mode
  '''
  # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
  # # if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
  # #   SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://")


class DevConfig(Config):
  '''
  Configurations for development
  '''

  DEBUG = True

config_options = {
  'development':DevConfig,
  'production' :ProdConfig
}