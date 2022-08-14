import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:

    DEBUG = False
    TESTING = False
    DEVELOPMENT = False

    SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(24))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'tododevdb.sqlite3')


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'todoproddb.sqlite3')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

        import logging
        from logging.handlers import SMTPHandler

        secure = None
        credentials = None

        app.logger.addHandler(mail_handler)


config = {
    'prod': ProductionConfig,
    'dev': DevelopmentConfig,
}
