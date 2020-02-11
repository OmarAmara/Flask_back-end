## imported modules
from flask import Flask, jsonify

## development
DEBUG = True
PORT = 8000 # hide in production/ when deploying, local env. now


app = Flask(__name__)

## routes
@app.route('/') # @ decorator
def index():
	return 'Hello World of Flask'

@app.route('/test_json')
def test_json_list():
	return jsonify(['hello', 'there', 'flaskers'])





## listener
if __name__ == '__main__':
	app.run(debug=DEBUG, port=PORT)