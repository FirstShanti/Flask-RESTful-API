from app import mongo
from flask import Blueprint, jsonify
from bson import ObjectId

# get user lit from mongo database collection
collection = mongo.db.get_collection('users')

users = Blueprint('users', __name__,)

# get list of users
@users.route('/users/', methods=['GET'])
def users_list():
	users = list(collection.find())
	if users:
		return jsonify({'message':'ok', 'data':users})
	else:
		return jsonify({'message':'error', 'data':'db is empty'}), 404

# get single user by id
@users.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
	if ObjectId.is_valid(user_id): 
		user = collection.find_one({'_id':ObjectId(user_id)})
		if user:
			return jsonify({'message':'ok', 'data':user})
		else:
			return jsonify({'message':'error', 'data':'user not found'}), 404
	else:
		return jsonify({'message':'error', 'data':'invalid user id'}), 404

# delete single user by id
@users.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
	if ObjectId.is_valid(user_id):
		if collection.find_one({'_id':ObjectId(user_id)}):
			collection.delete_one({'_id':ObjectId(user_id)})
			return jsonify({'message':'ok', 'data':{'status':'deleted', 'user':user_id}})
		else:
			return jsonify({'message':'error', 'data':'user not found'}), 404
	return jsonify({'message':'error', 'data':'invalid user id'}), 404
