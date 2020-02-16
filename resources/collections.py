import models
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

collections = Blueprint('collections', 'collections')

########## Routes ############

# Index
@collections.route('/', methods=['GET'])
def collections_index():
	try:
		collections = models.Collection.select()
		collections_dict = [model_to_dict(c) for c in collections]

		return jsonify(
			data=collections_dict,
			message=f"Retrieved {len(collections_dict)} collections.",
			status=200
		), 200
	except Exception as e:
		raise e

# Show
@collections.route('/<id>', methods=['GET'])	
def get_collection(id):
	try:
		collection = models.Collection.get_by_id(id)
		collection_dict = model_to_dict(collection)

		return jsonify(
			data=collection_dict,
			message=f"Found collection with id: {collection.id}.",
			status=200
		), 200
	except Exception as e:
		raise e


# Create
@collections.route('/', methods=['POST'])
def create_collection():
	try:
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

	except Exception as e:
		raise e

# Destroy
@collections.route('/<id>', methods=['Delete'])
def delete_collection(id):
	# TODO 2/15/20, 4:24 PM :Add logic to only let user delete their collections
	try:
		collection = models.Collection.get_by_id(id)
		collection.delete_instance()

		return jsonify(
	        data={}, 
	        message=f"Deleted collection with id: {id}",
	        status=200
      	), 200
	
	except Exception as e:
		raise e

# Update
@collections.route('/<id>', methods=['PUT'])
def update_collection(id):
	payload = request.get_json()

	collection = models.Collection.get_by_id(id)
	collection.name = payload['name'] if 'name' in payload else None
	collection.description = payload['description'] if 'description' in payload else None
	collection.category = payload['category'] if 'category' in payload else None

	collection.save()

	collection_dict = model_to_dict(collection)

	return jsonify(
		data=collection_dict,
		message=f'Updated collection with id: {collection.id}',
		status=200
	), 200	
	