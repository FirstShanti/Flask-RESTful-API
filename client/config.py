import os 

API_HOST = 'http://server:5000/api/'

class Configuration(object):
	DEBUG = os.environ.get('DEBUG')
	SECRET_KEY = 'secret_key'