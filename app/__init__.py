import os
from flask import Flask,request
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
bootstrap=Bootstrap(app)
app.config.from_object(Config)
db= SQLAlchemy(app)
migrate = Migrate(app, db)
app.debug = True

from app import models,routes
