import json
from flask import Flask, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient
from converter import MongoJSONEncoder, ObjectIdConverter
from config import Configuration

app = Flask(__name__)
app.config.from_object(Configuration)
mongo = PyMongo(app)

# converting mongodb ObjectId format to string
app.json_encoder = MongoJSONEncoder
app.url_map.converters['objectid'] = ObjectIdConverter

