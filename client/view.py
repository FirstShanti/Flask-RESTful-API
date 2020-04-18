import requests
from flask import Blueprint, redirect, render_template, flash
from config import DB_HOST

users = Blueprint('users', __name__, template_folder='templates')

@users.route('/users', methods=['GET'])
def user_list():
	data = requests.get(DB_HOST + 'users').json()
	return render_template('index.html', data=data)

@users.route('/users/<user_id>')
def get_user(user_id):
	user = requests.get(DB_HOST + f'users/{user_id}').json()
	return render_template('user_card.html', user=user)

@users.route('/users/delete/<user_id>')
def delete_user(user_id):
	res = requests.delete(DB_HOST + f'users/{user_id}').json()
	flash(res)
	return redirect('/users')