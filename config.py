import os
class Config:
  '''
  General configurations for the application
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/pitch_minute'
  SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
  '''
  Configurations for production mode
  '''
  # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
  # if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
  #   SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://")

class DevConfig(Config):
  '''
  Configurations for development
  '''

  DEBUG = True

config_options = {
  'development':DevConfig,
  'production' :ProdConfig
}