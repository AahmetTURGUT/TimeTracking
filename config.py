import os
BASEDIR =os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = 'postgres://ahmetturgut:Ahmet100$@postgres:5432/appdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
