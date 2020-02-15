from flask import Flask, jsonify


from resources.shows import shows

import models

DEBUG = True
PORT = 8000

app = Flask(__name__)

app.register_blueprint(shows, url_prefix='/api/v1/shows')

if __name__=='__main__':
	models.initialize()
	app.run(debug=DEBUG, port=PORT)
