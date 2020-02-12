### imported modules
# g allows use of global variables for life of this connection?
	# can be used to count connection and store in database?
	# somewhat relatable to app.locals in express servers
from flask import Flask, jsonify, g

# blueprint form ./resources/accounts
from resources.accounts import accounts

# helpful -- google: 'namespacing in python'
import models

"""# development #"""
DEBUG = True
PORT = 8000 # hide in production/ when deploying, local env. now


app = Flask(__name__)


# use blueprint (component/section of app) to handle accounts relatables
# analogous to app.use('/accounts', accountController) in express node servers
app.register_blueprint(accounts, url_prefix='/api/v1/accounts')


# decrease SQL connection pool:
# will connect to DB before every request, then close DB connection after every request
@app.before_request # this decorator specifically runs before requests
def before_request():
	"""Connect to the DB before each request"""
	# stores DB as a global var. in g
	g.db = models.DATABASE
	g.db.connect()

@app.after_request
def after_request():
	"""Closes the DB connection after each request"""
	g.db.close()
	# sends response back to client (in this app, JSON!)
	return response

## routes
@app.route('/') # @ decorator
def index():
	return 'Hello World of Flask'

@app.route('/test_json')
def test_json_list():
	return jsonify(['hello', 'there', 'flaskers'])

# (URL parameter)
@app.route('/welcome_message/<username>')
def welcome_message(username):
	return f'Hello, {username}. What are we having in our flask today? Anything to drink, maybe some CRUD?'





## listener
if __name__ == '__main__':
	# requiring DB before listener below. Sets-up tables in models.py
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
