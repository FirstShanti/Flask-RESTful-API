import requests
from flask import Blueprint, redirect, render_template, flash, abort, jsonify
from config import API_HOST

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/users/', methods=['GET'])
def user_list():
	res = requests.get(API_HOST + 'users')
	if res.status_code == 200:
		user_list = res.json()
		return render_template('index.html', data=user_list)
	abort(404, description="Invalid url")


@users.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
	res = requests.get(API_HOST + f'users/{user_id}')
	print('\n\nin get\n\n')
	if res.status_code == 200:
		user = res.json()
		return render_template('user_card.html', user=user)
	flash(f'User {user_id} not found')
	return redirect('/users')


@users.route('/users/delete/<user_id>', methods=['GET', 'DELETE'])
def delete_user(user_id):
	res = requests.delete(API_HOST + f'users/{user_id}')
	print('in delete')
	if res.status_code == 200:
		flash(f"user {res.json()['data']['user']} was deleted")
		return redirect('/users')
	flash(f'User {user_id} not found')
	return redirect('/users')
