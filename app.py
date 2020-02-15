from flask import Flask, jsonify, g


# from resources.show_collections import show_collections
from resources.collections import collections

import models

DEBUG = True
PORT = 8000

app = Flask(__name__)

# app.register_blueprint(show_collections, url_prefix='/api/v1/show_collections')
app.register_blueprint(collections, url_prefix='/api/v1/collections')

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
