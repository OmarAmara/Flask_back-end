## 'controller' file for Accounts
import models

from flask import Blueprint



# first arg. --> blueprint's name
# second arg. --> it's import_name
accounts = Blueprint('accounts', 'accounts')

@accounts.route('/')
def accounts_index():
	return "Hello, (accounts resource working properly)"