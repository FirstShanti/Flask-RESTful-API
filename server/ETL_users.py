import requests
from pymongo import MongoClient


client = MongoClient('mongo:27017/')
db = client.test_database
users = db.users


def fetch_data(count: int) -> list:
	res = requests.get(
		'https://randomuser.me/api/',
		params={
			'results':count,
			'gender':'male'})
	users.insert_many(res.json()['results'])
	return

if __name__=='__main__':
	fetch_data(100)
