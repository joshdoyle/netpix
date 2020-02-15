import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

collections = Blueprint('collections', 'collections')

########## Routes ############

# Index
@collections.route('/', methods=['GET'])
def collections_index():
	print('TELLY: in collections route')
	return "in collections index"

# Create
@collections.route('/', methods=['POST'])
def create_collection():
	payload = request.get_json()
	print(payload)
	
	collection = models.Collection.create(
		name = payload['name'],
		description = payload['description'],
		category = payload['category']
	)
	collection_dict = model_to_dict(collection)
	print('here is the collection:', collection_dict)
	return jsonify(
		data=collection_dict,
		status={'message': 'Created collection'}), 201