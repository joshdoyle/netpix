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
  		
class Show(Model):
	tmdb_id= IntegerField(unique=True)
	tmdb_title = CharField()
	tmdb_poster_path = CharField()
	tmdb_backdrop_path = CharField()
	tmdb_media_type = CharField()
	tmdb_overview = CharField()

	class Meta:
  		database = DATABASE

class ShowCollection(Model):
	collection_id = ForeignKeyField(Collection, backref='collections')
	show_id = ForeignKeyField(Show, backref='show_collections')
	user_description = CharField()

	class Meta:
  		database = DATABASE


########### Create tables ##########
def initialize():
	DATABASE.connect()

	# Only create tables if they don't exist (safe=True)
	DATABASE.create_tables([User, Collection, Show, ShowCollection], safe=True)

	DATABASE.close()

