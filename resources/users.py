# This file is similar to User/ Auth Controller in node.js express servers
import models

from flask import Blueprint

# create users blueprint
users = Blueprint('users', 'users')


## Users routes

# user index route
@users.route('/', methods=['GET'])
def testing_user_resource():
	return 'Yay to properly setting up User Resources!'