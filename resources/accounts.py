## 'controller' file for Accounts
import models

# request -- this sends client's request to global request object
# reassigns on every request containing a body
from flask import Blueprint, request, jsonify # jsonify needed to interperate JSON from request body

from flask_login import current_user

# will print table on console legibly...
from playhouse.shortcuts import model_to_dict


# first arg. --> blueprint's name
# second arg. --> it's import_name
accounts = Blueprint('accounts', 'accounts')

### Account routes

# account index
@accounts.route('/', methods=['GET'])
def accounts_index():
	"""Get all Accounts from the DB as JSON"""
	# all_accounts_query = models.Account.select()

	# we need a list of dictionaries...
	#changed to only display created accounts by user logged in
	current_user_account_dicts = [model_to_dict(account) for account in current_user.accounts]

	print(current_user_account_dicts)

	return jsonify(
		data=current_user_account_dicts,
		message=f'Successfully retrieved {len(current_user_account_dicts)} Accounts',
		status=200
	), 200

# account create route
@accounts.route('/', methods=['POST'])
def create_account():
	# .get_json() attaches to request object and extracts JSON from the request body
	# similar to req.body in express servers!
	payload = request.get_json()
	print('\n', payload) # prints request data on terminal
	# utilizes peewee model to add to DB
	account = models.Account.create(
		institution=current_user.id, 
		name=payload['name'], 
		balance=payload['balance'])
	print(account) # just prints ID, utilize: sqlite3 --> 'sqlite3 accounts.sqlite'
	print(account.__dict__) # class attribute __dict__--> makes info useful!

	# print(dir(account)) # prints ALL property methods(can be useful, just annoying (and PTSD from method callback error stack) for now)

	# note: you cannot directly jsonify account b/c it's not a dictionary or jsonifiable object
		# this would cause an error --> TypeError: Object of type 'Account' is not JSON serializable

	# model_to_dict, from playhouse, converts mordel to a dict.
	account_dict = model_to_dict(account)

	account_dict['institution'].pop('password')

	return jsonify(
		data=account_dict,
		message='Successfully created Account!',
		status=201,
	), 201

# account delete/destroy route
@accounts.route('/<id>', methods=['Delete'])
def delete_account(id):
	# deleting data based on id identifier
	delete_query = models.Account.delete().where(models.Account.id == id)
	delete_query.execute()
	return jsonify(
		data={},
		message=f'Successfully deleted Account with id {id}',
		status=200
	), 200


# account update/ edit PUT route
@accounts.route('/<id>', methods=['PUT'])
def update_account(id):
	payload = request.get_json()
	# unpack operator * & **: https://codeyarns.github.io/tech/2012-04-25-unpack-operator-in-python.html
	update_query = models.Account.update(**payload).where(models.Account.id == id)

	update_query.execute()

	# (benefits front end to retrive this)
	update_account = models.Account.get_by_id(id)

	return jsonify(
 		data=model_to_dict(update_account),
  		message=f'Successfully updated account with id {id}',
  		status=200
	), 200


# route to create account associated with institution that has the id
@accounts.route('/<institution_id>', methods=['POST'])
def create_account_with_institution(institution_id):
	payload = request.get_json()
	print(payload)

	# creat account with associated <institution_id>
	account = models.Account.create(
		institution=institution_id,
		name=payload['name'],
		balance=payload['balance']
	)

	account_dict = model_to_dict(account)

	print(account_dict) # see how institution is attached

	# remove password from user in isntitution
	account_dict['institution'].pop('password')

	return jsonify(
		data=account_dict,
		message="Successfully created account",
		status=201
	), 201


