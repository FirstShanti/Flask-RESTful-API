import requests
from flask import (
	Flask,
	request,
	render_template,
	Blueprint,
	redirect,
	flash
)

app = Flask(__name__)
app.config.from_object('config')
app.config['SECRET_KEY'] = 'secret_key'

users = Blueprint('users', __name__, template_folder='templates')

@users.route('/users', methods=['GET'])
def user_list():
	data = requests.get('http://localhost:5000/users').json()

	return render_template('index.html', data=data)

@users.route('/users/<user_id>')
def get_user(user_id):
	user = requests.get(f'http://localhost:5000/users/{user_id}').json()
	return render_template('user_card.html', user=user)

@users.route('/users/delete/<user_id>')
def delete_user(user_id):
	res = requests.delete(f'http://localhost:5000/users/{user_id}').json()
	flash(res)
	return redirect('/users')

app.register_blueprint(users, url_prefix='/')

if __name__=='__main__':
	app.run(port=5001)