# Flask_back-end

## Tutorial for creating a Flask Back-end API -- this one will be for accounts! Not that you would like to share your accounts, legally.

-	run 'pip3 install -r requirements.txt' to retrieve/ install modules from repo.

```bash
$ pip3 install -r requirements.txt
```

step 0: 
	create(for python): .gitignore --> .env & other relatables

step 1: 
	run: 'virtualenv .env -p python3'

step 2: 
	run: 'source .env/bin/activate' **(see notes below: need to 'deactivate' environment when done)

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

step 7: 
	jsonify

step 8: 
	install peewee & psycopg2/ run: 'pip3 install pewee psycopg2' re-run: 'pip3 freeze > requirements.txt'

step 9: 
	initialize database tables and connections in models.py file, then import and initialize in app.py.

step 10: 
	Create a resource folder for accounts, set-up for account routes(controllers). Import resources/blueprint and register blueprint (as middleware like controller)

step 11: 
	Import request from flask into account.py resources to use request object data; json, form data,... and use .get_json() to extract/utilize JSON data. Since we are using JSON as request body data, import jsonify from flask as well.

	Import 'g' from flask in app.py for utilizing global variable to have access to DB and request body. Create before/after_request routes to efficiently utilize Database connection pool.


step 12: 
	Back to account.py --> import model_to_dict from playhouse.shortcuts(brought to you by peewee!). This will make the data we retrieve from body jsonifiable. Use peewee model to create form data on to DB. Then we will use playhouse...

****{Now we will be transitioning to the react-app-accounts repository in OAmara GitHub to start implementing a front end react app to show and add to this API. If you are only interested in creating the API without a fron end then skip this process.}
***{I highly encourage you to look at the react-app-accounts before continuing as it will help you with your understanding with why we need to implement the changes/ additions in the following steps: }

step 13:
	


note: - ******* run: 'deactivate'. To leave virtual environment. - always run 'pip3 freeze > requirements.txt' after installing a module. - run 'pip3 install -r requirements.txt' to retrieve/ install modules from repo.
