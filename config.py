import os

DIALECT = 'mysql'
DIRVER = 'pymysql' # DIRVER = 'mysqldb'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '192.168.10.70'
PORT = '3306'
DATABASE = 'earth_test'
DB_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format (DIALECT,
        DIRVER, USERNAME, PASSWORD, HOST, PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

DEBUG = True
SECRET_KEY = os.urandom(24)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# import osauto
#
# basedir = os.path.abspath(os.path.dirname(__file__))
#
#
# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
#     SQLALCHEMY_COMMIT_ON_TEARDOWN = True
#     FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
#     FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
#     FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
#
#     @staticmethod
#
#     // 此注释可表明使用类名可以直接调用该方法
#
#     def init_app(app): //
#
#         执行当前需要的环境的初始化
#     pass
#
#
# class DevelopmentConfig(Config):
#
#
#     # 开发环境
# DEBUG = True
# MAIL_SERVER = 'smtp.googlemail.com'
# MAIL_PORT = 587
# MAIL_USE_TLS = True
# MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
# MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
# SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
#                           'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
#
#
# class TestingConfig(Config):
#
#
#     # 测试环境
# TESTING = True
# SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
#                           'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')
#
#
# class ProductionConfig(Config): //
#
#
#     # 生产环境
# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#                           'sqlite:///' + os.path.join(basedir, 'data.sqlite')
#
# config = {
#     'development': DevelopmentConfig,
#     'testing': TestingConfig,
#     'production': ProductionConfig,
#     'default': DevelopmentConfig
# }
