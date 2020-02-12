## 'controller' file for Accounts
import models

from flask import Blueprint



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
	return "you hit account create route"