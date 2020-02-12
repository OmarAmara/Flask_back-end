### imported modules
# g allows use of global variables for life of this connection?
	# can be used to count connection and store in database?
	# somewhat relatable to app.locals in express servers
from flask import Flask, jsonify, g

# package that will allow us to handle CORS
# https://flask-cors.readthedocs.io/en/latest/
from flask_cors import CORS

# blueprint form ./resources/accounts
from resources.accounts import accounts

# helpful -- google: 'namespacing in python'
import models

"""# development #"""
DEBUG = True
PORT = 8000 # hide in production/ when deploying, local env. now


app = Flask(__name__)


# note: A domain name is considered an 'origin', currently our 'origin' for the development api server
# is localhost:... ; otherwise, it would be a hosted url. Same would go for the server that would
# try to access the API. This in a way 'sets expectations of who to connect/ hear from'
# arguments in order:
	# 1. add cors to blueprint, 2. list of allowed origins, 3. allows reqs. with cookies attached, allowing sessions for auth.
CORS(dogs, origins=['http://localhost:3000'], supports_credentials=True)


# use blueprint (component/section of app) to handle accounts relatables, set controllers
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
def after_request(response):
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
