from flask import Flask, jsonify, g
from flask_login import LoginManager
import config

from resources.collections import collections
from resources.show_collections import show_collections
from resources.shows import shows
from resources.search import search
from resources.users import users

import models

DEBUG = True
PORT = 8000

app = Flask(__name__)

# Login setup
app.secret_key = config.APP_SECRET_KEY
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(userid):
	try:
		return models.User.get(models.User.id == userid)
	except models.DoesNotExist:
		return None

@login_manager.unauthorized_handler
def unauthorized():
	return jsonify(
		data={
			'error': 'User not logged in.'
			},
		message='You must be logged in the access that resource.',
		status=401
		), 401			


app.register_blueprint(show_collections, url_prefix='/api/v1/show_collections')
app.register_blueprint(collections, url_prefix='/api/v1/collections')
app.register_blueprint(shows, url_prefix='/api/v1/shows')
app.register_blueprint(search, url_prefix='/api/v1/search')
app.register_blueprint(users, url_prefix='/api/v1/users')

@app.before_request
def before_request():
	g.db = models.DATABASE
	g.db.connect()

@app.after_request
def after_request(response):
	g.db.close()
	return response	

if __name__=='__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
