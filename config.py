import os
class Config:
  '''
  General configurations for the application
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:access@localhost/minute_pitch'
  SECRET_KEY = os.environ.get('SECRET_KEY')

class ProdConfig(Config):
  '''
  Configurations for production mode
  '''
  pass

class DevConfig(Config):
  '''
  Configurations for development
  '''

  DEBUG = True

config_options = {
  'development':DevConfig,
  'production' :ProdConfig
}