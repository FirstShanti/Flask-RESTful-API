import requests
from flask import Blueprint, redirect, render_template, flash, abort, jsonify
from config import DB_HOST

users = Blueprint('users', __name__, template_folder='templates')


@users.route('/users', methods=['GET'])
def user_list():
	res = requests.get(DB_HOST + 'users')
	if res.status_code == 200:
		user_list = res.json()['data']
		return render_template('index.html', data=user_list)
	abort(404, description="Invalid url")


@users.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
	res = requests.get(DB_HOST + f'users/{user_id}')
	if res.status_code == 200:
		user = res.json()['data']
		return render_template('user_card.html', user=user)
	abort(404, description="User not found")


@users.route('/users/delete/<user_id>', methods=['GET'])
def delete_user(user_id):
	res = requests.delete(DB_HOST + f'users/{user_id}')
	if res.status_code == 200:
		flash(f"user {res.json()['data']['user']} was deleted")
		return redirect('/users')
	abort(404, description="User not found")
