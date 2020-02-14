# This file is similar to User/ Auth Controller in node.js express servers
import models

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
# enables sessions(cookies)
from flask_login import login_user, current_user
from playhouse.shortcuts import model_to_dict

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
		### Make logic to not create existing username as well

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

		# flask_login: "logs in" user/ starts a session.
		login_user(created_user)

		user_dict = model_to_dict(created_user)
		print(user_dict) # created user

		# IF we want to send encrypted password back, would have to convert due to it not being a string, but now a 'byte'
		# do not want to send encrypted password string back to user.
		user_dict.pop('password')

		return jsonify(
			data=user_dict,
			message=f"Successfully registered {user_dict['email']}",
			status=201
		), 201


# user login POST route
@users.route('/login', methods=['POST'])
def login():
	payload = request.get_json()

	payload['email'] = payload['email'].lower()
	payload['username'] = payload['username'].lower()

	try:
		# find user by email
		user = models.User.get(models.User.email == payload['email'].lower())

		# if email was found, THEN compare to password
		user_dict = model_to_dict(user)
		# use bcrypt to check password:
		# 1st arg = encryp password being checked against using check_password_hash
		# 2nd arg = password attempt provided by user
		password_to_compare = check_password_hash(user_dict['password'], payload['password'])

		# if password comparison matches
		if password_to_compare:
			# create login session
			login_user(user)

			# remove password to not display with data
			user_dict.pop('password')

			return jsonify(
				data=user_dict,
				message=f"Successfully logged in to API: {user_dict}",
				status=200
			), 200

		else:
			# seen in server/ back-end
			print('Password does not match')
			return jsonify(
				data={},
				message="Email or password is incorrect",
				status=401
			), 401

	# user not found
	except models.DoesNotExist:
		print('Username/ Email does not match')
		return jsonify(
			data={},
			message='Email or Password is incorrect',
			status=401
		), 401


# Delete This Route After development:
# User index
@users.route('/all', methods=['GET'])
def user_index():
	users = models.User.select()

	user_dicts = [model_to_dict(u) for u in users]

	# queery retrieves user passwords as well. Following function will take out passwords before showing data.
	def remove_password(u):
		u.pop('password')
		return u

	user_dicts_without_pw = map(remove_password, user_dicts)

	return jsonify(data=list(user_dicts_without_pw)), 200




# demonstration of current_user session use
# requires user_loader to be set in app.py
@users.route('/logged_in', methods=['GET'])
def get_logged_in_user():
	# IMPORTANT READ: https://flask-login.readthedocs.io/en/latest/#flask_login.current_user
	print(current_user) # logged in user
	user_dict = model_to_dict(current_user)
	print(user_dict)
	return jsonify(data=user_dict), 200



