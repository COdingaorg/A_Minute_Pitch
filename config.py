class Config:
  '''
  General configurations for the application
  '''
  pass

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