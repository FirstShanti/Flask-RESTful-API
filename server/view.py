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
	return jsonify(users)

# get single user by id
@users.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
	if ObjectId.is_valid(user_id): 
		user = collection.find_one({'_id':ObjectId(user_id)})
		return jsonify(user or {'message':'user not found'})
	else:
		return jsonify({'message':'invalid user id'})

# delete single user by id
@users.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
	if ObjectId.is_valid(user_id):
		if collection.find_one({'_id':ObjectId(user_id)}):
			collection.delete_one({'_id':ObjectId(user_id)})
			return jsonify({'message':f'user {user_id} was deleted'})
		else:
			return jsonify({'message':'user not found'})
	return jsonify({'message':'invalid user id'})

# 404 error page handler
@users.errorhandler(404)
def page_not_found(error):
    return jsonify({'message':'page not found'})