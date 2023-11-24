import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    FLASKY_ADMIN_A = '2272393014@qq.com'
    FLASKY_ADMIN_B = '1104028870@qq.com'
    FLASKY_ADMIN_C = ''
    FLASKY_ADMIN_D = ''
    FLASKY_ADMIN_E = ''
    FLASKY_ADMIN_F = ''

    UPLOAD_FOLDER = 'front_end/tabibito_frontend/dist/pictures'
    UPLOAD_URL = 'pictures'
    BASE_URL = "http://127.0.0.1:5000"
    # BASE_URL = "http://csi420-01-vm1.ucd.ie/"
    AVATAR_FOLDER = 'front_end/tabibito_frontend/dist/pictures'
    AVATAR_URL = 'avatar'



    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SAMESITE = None
    SESSION_COOKIE_SECURE = False

    # 数据库的配置变量
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'tabibito'
    USERNAME = 'root'
    # PASSWORD = 'Wangji1208'
    PASSWORD = 'l20011026'
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_POOL_RECYCLE = 28800

    SECRET_KEY = 'mou107b6vsfxor82bbc4bzf4mcu7'


    # email config
    # use 163 email
    MAIL_SERVER = "smtp.163.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEBUG = True
    MAIL_USERNAME = "tabibito_1@163.com"
    MAIL_PASSWORD = "INKSISDGQFZCIQLS"
    MAIL_DEFAULT_SENDER = "tabibito_1@163.com"

class TestingConfig(Config):
    TESTING = True
    # SQLALCHEMY_DATABASE_URI = \
    #     "sqlite:///" + os.path.join(basedir, "data.sqlite")
    # SQLALCHEMY_TRACK_MODIFICATIONS = True


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    # SQLALCHEMY_DATABASE_URI = \
    #     "sqlite:///" + os.path.join(basedir, "data.sqlite")
    # SQLALCHEMY_TRACK_MODIFICATIONS = True


class ThirdConfig(Config):
    WEATHER_URL = "http://api.weatherapi.com/v1"
    WEATHER_KEY = "9fa81e39ed22488fa10104307230905"
    FLIGHT_URL = "https://aeroapi.flightaware.com/aeroapi/flights/"
    FLIGHT_KEY = "yaBZdh4pjUvChVtNh8OoFcfAzbMfapTI"


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}