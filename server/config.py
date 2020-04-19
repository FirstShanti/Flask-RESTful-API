import os

COUNT_USERS = os.environ.get('COUNT_USERS')
GENDER = os.environ.get('GENDER')

class Configuration(object):
	DEBUG = os.environ.get('DEBUG')
	MONGO_URI = 'mongodb://mongo:27017/test_database'