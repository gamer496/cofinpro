from app import app, db
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import uuid
import ipdb
import random
import string
from hashlib import sha512

SIMPLE_CHARS = string.ascii_letters + string.digits

def get_random_string(length = 40):
    return ''.join(random.choice(SIMPLE_CHARS) for i in xrange(length))

def gen_id(length = 40):
    hash = sha512()
    hash.update(get_random_string())
    return hash.hexdigest()[:length]

class MajorUser(db.Model):
    __tablename__ = "major_user"
    id              =db.Column      (db.Integer, primary_key = True)
    name            =db.Column      (db.String(200))
    search_queries  =db.relationship("SearchQuery", backref = "user", lazy = "dynamic")

    def __init__(self):
        self.name = " some"

    def __repr__(self):
        return "User: " + self.id

class SearchQuery(db.Model):
    __tablename__ = "search_query"
    id          =db.Column      (db.Integer, primary_key = True)
    content     =db.Column      (db.String(250))
    queried_on  =db.Column      (db.DateTime)
    executed_on =db.Column      (db.DateTime)
    user_id     =db.Column      (db.Integer, db.ForeignKey(MajorUser.id))

    def __init__(self, content):
        self.content = content
        self.queried_on = datetime.utcnow()

    def __repr__(self):
        return "Query: " + self.content
