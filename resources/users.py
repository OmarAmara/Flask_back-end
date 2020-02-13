# This file is similar to User/ Auth Controller in node.js express servers
import models

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash

# create users blueprint
users = Blueprint('users', 'users')


## Users routes

# user index route
@users.route('/', methods=['GET'])
def testing_user_resource():
	return 'Yay to properly setting up User Resources!'


# user register route
@users.route('/register', methods=['POST'])
def register():
	payload = request.get_json()

	# makes emails/ usernames case insensitive,...emails are traditionally case insensitive and will be used for login auth.
	payload['email'] = payload['email'].lower()
	payload['username'] = payload['username'].lower()
	print(payload)

	try:
		# check in DB if user exists, if they do, then do not create.
		models.User.get(models.User.email == payload['email'])
		# result throws a 'models.DoesNotExist exception' error.

		# if no error was caused, then username already exists
		return jsonify(
			data={},
			message='A User with that email already exists',
			status=401
		), 401

	# if resulted in '..DoesNotExist' error, then register new user
	except models.DoesNotExist: # similar to catch in JavaScript

		created_user = models.User.create(
			username=payload['username'],
			email=payload['email'],
			password=generate_password_hash(payload['password'])
		)

		return jsonify(
			data=created_user,
			message=f'Successfully registered user',
			status=201
		), 201






