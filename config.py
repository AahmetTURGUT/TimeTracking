import os
BASEDIR =os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Ahmet100$@localhost/appdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
