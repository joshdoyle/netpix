import datetime
from peewee import *

DATABASE = SqliteDatabase('telly.sqlite')

############# Models ####################
class User(Model):
	username = CharField(unique=True)
	email = CharField(unique=True) 
	password = CharField()

	class Meta:
  		database = DATABASE

class Collection(Model):
	name = CharField()
	description = CharField()
	category = CharField()

	class Meta:
  		database = DATABASE
  		
# Show will be both tv shows and movies
class Show(Model):
	apiShow_id = CharField(unique=True)
	apiEpisode_id = CharField(unique=True)

	class Meta:
  		database = DATABASE

class ShowCollection(Model):
	collection_id = ForeignKeyField(Collection, backref='ShowCollection')
	show_id = ForeignKeyField(Show, backref='ShowCollection')
	user_description = CharField(unique=True)
	order = IntegerField()

	class Meta:
  		database = DATABASE


########### Create tables ##########
def initialize():
	DATABASE.connect()

	# Only create tables if they don't exist (safe=True)
	DATABASE.create_tables([User, Collection, ShowCollection, Show], safe=True)

	DATABASE.close()

