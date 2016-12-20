from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
db = SQLAlchemy(app)
manager = Manager(app)
app.config.from_object('config')
migrate = Migrate(app, db)
CORS(app)
auth = HTTPBasicAuth()

from app import models, views
