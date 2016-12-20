from app import app, db, auth
from models import *
from flask import jsonify, request
import os
from datetime import datetime
import json
import random
import ipdb


@app.errorhandler(404)
def page_not_found(e = ""):
    return jsonify({"err": "page not found " + e}), 404

@app.errorhandler(403)
def not_authorized(e = ""):
    return jsonify({"err": "you are not authorized to see this page " + e}), 403

@app.errorhandler(500)
def internal_error(e = ""):
    return jsonify({"err": "internal error occured. Check server logs " + e}),500

@app.errorhandler(400)
def something_missing(e = ""):
    return jsonify({"err": "arguments provided were not enough to carry out this request " + e}), 400

@app.route("/index", methods = ["GET", "POST"])
def index():
    return jsonify({"msg": "kamehameha"})

@app.route("/game_query", methods = ["POST"])
def game_query():
    try:
        data = request.json
    except:
        return page_not_found()
    user = data["user"].strip()
    if user == "new":
        user = MajorUser()
        db.session.add(user)
        db.session.commit()
    else:
        user = MajorUser.query.get(user)
        if not user:
            return jsonify({"err": "no such user found"})
    content = data["content"]
    sq = SearchQuery(content = content)
    db.session.add(sq)
    sq.user_id = user.id
    db.session.commit()
    #get the recommendation
    return jsonify({"datas": ["ok", "ok1"]})
