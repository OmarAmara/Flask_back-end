## 'controller' file for Accounts
import models

# request -- this sends client's request to global request object
# reassigns on every request containing a body
from flask import Blueprint, request, jsonify # jsonify needed to interperate JSON from request body



# first arg. --> blueprint's name
# second arg. --> it's import_name
accounts = Blueprint('accounts', 'accounts')

### Account routes

# account index
@accounts.route('/', methods=['GET'])
def accounts_index():
	return "Hello, (accounts resource working properly)"

# account create route
@accounts.route('/', methods=['POST'])
def create_account():
	# .get_json() attaches to request object and extracts JSON from the request body
	# similar to req.body in express servers!
	payload = request.get_json()
	print(payload) # prints request data on terminal
	return "you hit account create route"

