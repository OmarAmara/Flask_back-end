step 0:
		create(for python): .gitignore      --> .env & other relatables

step 1:
		run: 'virtualenv .env -p python3'

step 2:
		run: 'source .env/bin/activate'
		**(see notes below: need to 'deactivate' environment when done)

step 3:
		run: 'pip3 install flask'

step 4:
		run: 'pip3 freeze > requirements.txt'

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

step 7: jsonify

step 8:
	install peewee & psycopg2/ run: 'pip3 install pewee psycopg2'
	re-run: 'pip3 freeze > requirements.txt'

step 9:
	initialize database tables and connections in models.py file, then import and initialize in app.py.

step 10:
	Create a resource folder for accounts, set-up for account routes(controllers). Import resources/blueprint and register blueprint (as middleware like controller)







note: 
	-	******* run: 'deactivate'. To leave virtual environment.
	-	always run 'pip3 freeze > requirements.txt' after installing a module.
	-	run 'pip3 install -r requirements.txt' to retrieve/ install modules from repo.

