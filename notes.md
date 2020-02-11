step 0:
		.gitignore      --> .env

step 1:
		virtualenv .env -p python3

step 2:
		source .env/bin/activate

step 3:
		pip3 install flask

step 4:
		pip3 freeze > requirements.txt

step 5:
	Program server --> then run command in CLI UI: 'python3 app.py' (python_runtime_environment & python_file_name).

	note: should see something similar to --
		 * Serving Flask app "app" (lazy loading)
 		 * Environment: production
		   WARNING: This is a development server. Do not use it in a production deployment.
		   Use a production WSGI server instead.
		 * Debug mode: on
		 * Running on http://....(irrelevant number):8000/ (Press CTRL+C to quit)
		 * Restarting with stat
		 * Debugger is active!
		 * Debugger PIN

step 6:
	Create routes and confirm by running server as in step 5 and go to route in browser or postman(app).

	note: To confirm that it works, you should see the message being returned in the browser and a line pop-up in terminal confirming hitting port, date and route with status code.

7: jsonify






