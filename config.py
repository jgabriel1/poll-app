class Config:
    ENV = 'production'
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'supersecret'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./default.db'
    TEMPLATE_AUTO_RELOAD = True


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/poll_app'


class TestingConfig(Config):
    ENV = 'testing'
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./test.db'
