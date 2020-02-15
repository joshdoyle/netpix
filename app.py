from flask import Flask, jsonify


from resources.show_collections import show_collections

import models

DEBUG = True
PORT = 8000

app = Flask(__name__)

app.register_blueprint(show_collections, url_prefix='/api/v1/show_collections')

if __name__=='__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
