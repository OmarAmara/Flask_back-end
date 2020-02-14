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
	change returned data in routes to return a json object from jsonify.

step 14:
	install and import flask_cors module to enter origin acceptions and enable use of session authentication:
	run in console CLI: 'pip3 install flask_cors' (don't forget to run 'pip3 freeze > requirements.txt' afterward).

step 15:
	Import CORS from flask_cors in app.py.
	Set CORS parameters: CORS({add to blueprint: insert blueprint name}, {origins accepted: origin name, in our case, localhost:...}, {whether it accepts credentials/ sessions: Boolean}) --> see code in app.py for details

-- CHECK COMMITS --

step 16:
	We will enable our API to delete data by creating a destroy route.

step 17:
	We will ad an update route for fron end apps to be able to update data on API.

step 18 -- We will be adding authentication:
	Install following: 'pip3 install flask_login flask-bcrypt' (dont forget about updating requirements.txt!)

step 19:
	import flask_login to models file in order to create User model and tables. This will enable us to easily set-up User class methods, session/ login auth functionality.

step 20:
	In Models.py, import UserMixin from flask_login and use this to create User Class. 
	Connect user to same DB(Database) and set-up table creation.

step 21:
	Import and set-up LoginManager from flask_login in app.py file. This will be our secret tool that enables session/login.
	Set secret_key string and instantiate, then connect LoginManager to app.

step 22:
	Create users.py file in resources and import model, blueprint then start making routes. Let's just make a test index route for now.
	Set-up users resource, blueprint and give access to origins in app.py.

step 23:
	(routes) Let's create a register route that will create a user, verify proper credentials and query if user already exists, encrypts password and sends json data to return a success/ error message. Check commit for imports.

step 24:
	Now set-up a login route for existing users that will work similarly as the register route.

step 25:
	We will now be creating a one to many relationship with accounts. How can we do this without refacotoring our code? Maybe institutions/ banks will contain accounts? Other ideas? ForeignKey will be utilized and backreference to banks.

step 26:
	Create helper route for users index. Use only for development to view all users.

step 27:
	Make route under accounts.py that will allow a user to create account when logged in...

step 28:
	Create route under model that contains foreign key so that a specific user_id, this will be user who is logged in creating the account, becomes associated through institution.

step 29:
	Include user_loader from login_manager in app.py. This will allow us to access login_user object (session/ cookie object).

step 30:
	Have model account created route create account based on who is logged in.

step 31:
	Create logout route since session/cookie/login_manager data is not destroyed when server restarts unlike express servers.

note: - ******* run: 'deactivate'. To leave virtual environment. - always run 'pip3 freeze > requirements.txt' after installing a module. - run 'pip3 install -r requirements.txt' to retrieve/ install modules from repo.

