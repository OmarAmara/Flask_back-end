# imported modules
from flask import Flask

# development
DEBUG = True
PORT = 8000 # hide in production/ when deploying, local env. now

app = Flask(__name__)









# listener
if __name__ == '__main__':
	app.run(debug=DEBUG, port=PORT)