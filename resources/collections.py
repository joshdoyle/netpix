import models
from flask import Blueprint, request

collections = Blueprint('collections', 'collections')


@collections.route('/', methods=['GET'])
def collections_index():
	print('TELLY: in collections route')
	return "in collections index"

# This route probably won't be part of api. Putting here for test
@collections.route('/', methods=['POST'])
def create_collection():
	payload = request.get_json()
	print(payload)
	return 'in collections create route'