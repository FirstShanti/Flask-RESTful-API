from app import collection
from flask import Blueprint, jsonify
from bson import ObjectId

users = Blueprint('users', __name__,)

@users.route('/users/', methods=['GET'])
def users_list():
	users = list(collection.find())
	return jsonify(users)


@users.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
	if ObjectId.is_valid(user_id): 
		user = collection.find_one({'_id':ObjectId(user_id)})
		return jsonify(user or {'message':'user not found'})
	else:
		return jsonify({'message':'invalid user id'})


@users.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
	if ObjectId.is_valid(user_id):
		if collection.find_one({'_id':ObjectId(user_id)}):
			collection.delete_one({'_id':ObjectId(user_id)})
			return jsonify({'message':f'user {user_id} was deleted'})
		else:
			return jsonify({'message':'user not found'})
	return jsonify({'message':'invalid user id'})


@users.errorhandler(404)
def page_not_found(error):
    return jsonify({'message':'page not found'})