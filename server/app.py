import json
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient
from converter import MongoJSONEncoder, ObjectIdConverter


app = Flask(__name__)

app.config["MONGO_URI"] = 'mongodb://mongo:27017/test_database'
mongo = PyMongo(app)

app.json_encoder = MongoJSONEncoder
app.url_map.converters['objectid'] = ObjectIdConverter

collection = mongo.db.get_collection('users')

