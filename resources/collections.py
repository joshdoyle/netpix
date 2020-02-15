import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

collections = Blueprint('collections', 'collections')

########## Routes ############

# Index
@collections.route('/', methods=['GET'])
def collections_index():
	collections = models.Collection.select()
	collections_dict = [model_to_dict(c) for c in collections]

	return jsonify(
		data=collections_dict,
		message=f"Retrieved {len(collections_dict)} collections.",
		status=200
	), 200

# Show
@collections.route('/<id>', methods=['GET'])	
def get_collection(id):
	collection = models.Collection.get_by_id(id)
	collection_dict = model_to_dict(collection)

	return jsonify(
		data=collection_dict,
		message=f"Found collection with id: {collection.id}.",
		status=200
	), 200


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
		status={'message': 'Created collection'}
	), 201