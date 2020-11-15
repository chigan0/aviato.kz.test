from sys import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from settings import Config

path.append(Config.BASE_DIR)
app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)
db = SQLAlchemy(app)

