from config.default import ConfigDefault

class DesarrolloConfig(ConfigDefault):
    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'sqlite:///films.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SHOW_SQLALCHEMY_LOG_MESSAGES = False
    ERROR_404_HELP = False