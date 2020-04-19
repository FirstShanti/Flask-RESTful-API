import requests
from pymongo import MongoClient
from config import COUNT_USERS, GENDER

client = MongoClient('mongo:27017')
db = client.test_database
users = db.users
users.remove({})

def fetch_data():
	res = requests.get(
		'https://randomuser.me/api/',
		params={
			'results':COUNT_USERS,
			'gender':GENDER})
	users.insert_many(res.json()['results'])




