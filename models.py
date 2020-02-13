### all models file

## modules
import datetime
# peewee (similar to mongoose)
# import *, imports everything! including:
	# SqliteDatabase (adapter)
	# Model -- Model() class

from peewee import *

# UserMixin helpful for creating User model with fucntions.
# flask_login will also enable us to set-up session(cookies)/login authentication
# https://flask-login.readthedocs.io/en/latest/
from flask_login import UserMixin


#### .gitignore DB connection during deployment, outside of local virtual env.
## change to psql later for deployment
# portable data for development
# value: Database connection string
DATABASE = SqliteDatabase('accounts.sqlite')



# UserMixin brings some additional methods and properties into the mix!
# provides Model Class methods that peewee Model class does not provide.
# see: https://flask-login.readthedocs.io/en/latest/#your-user-class
class User(UserMixin, Model):
	username = CharField(unique=True)
	email = CharField(unique=True)
	password = Charfield()

	class Meta:
		database = DATABASE



# helpful: http://docs.peewee-orm.com/en/latest/peewee/models.html#
## Defining Account model
class Account(Model):
	institution = CharField() # associated bank
	name = CharField()
	balance = IntegerField()
	created_at = DateTimeField(default=datetime.datetime.now)

	# specialized constructor to specify to class how to connect to DB
	class Meta:
		database = DATABASE




# method called in app.py to set-up DBs connection
def initialize():
	DATABASE.connect()


DATABASE.create_tables([User, Account], safe=True)
print('Connected to DB and created tables if non-existed')


## close DB connection to free space in connection pool
# more specific to SQL DBs,
DATABASE.close()
