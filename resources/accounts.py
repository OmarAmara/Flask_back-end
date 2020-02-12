## 'controller' file for Accounts
import models

# request -- this sends client's request to global request object
# reassigns on every request containing a body
from flask import Blueprint, request, jsonify # jsonify needed to interperate JSON from request body

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
	all_accounts_query = models.Account.select()

	# we need a list of dictionaries...
	account_dicts = [model_to_dict(d) for d in all_accounts_query]

	return jsonify(
		data=account_dicts,
		message=f'Successfully retrieved {len(account_dicts)} Accounts',
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
	account = models.Account.create(institution=payload['institution'], name=payload['name'], balance=payload['balance'])
	print(account) # just prints ID, utilize: sqlite3 --> 'sqlite3 accounts.sqlite'
	print(account.__dict__) # class attribute __dict__--> makes info useful!

	# print(dir(account)) # prints ALL property methods(can be useful, just annoying (and PTSD from method callback error stack) for now)

	# note: you cannot directly jsonify account b/c it's not a dictionary or jsonifiable object
		# this would cause an error --> TypeError: Object of type 'Account' is not JSON serializable

	# model_to_dict, from playhouse, converts mordel to a dict.
	account_dicts = model_to_dict(account)

	return jsonify(
		data=account_dicts,
		message='Successfully created Account!',
		status=201,
	), 201

