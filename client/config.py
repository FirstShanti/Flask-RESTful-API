import os 

DB_HOST = 'http://server:5000/'

class Configuration(object):
	DEBUG = os.environ.get('DEBUG')
	SECRET_KEY = 'secret_key'