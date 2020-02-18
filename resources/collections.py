import models
from models import Collection, ShowCollection, Show
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

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
	except models.Collection.DoesNotExist:
		return jsonify(
			message=f"Collection: {id} does not exist.",
			status=204
		), 204


# Create
@collections.route('/', methods=['POST'])
@login_required
def create_collection():
	try:
		payload = request.get_json()
		collection = models.Collection.create(
			name = payload['name'],
			description = payload['description'],
			category = payload['category'],
			user_id = current_user.id
		)
		collection_dict = model_to_dict(collection)

		return jsonify(
			data=collection_dict,
			status={'message': 'Created collection'}
		), 201

	except Exception as e:
		raise e

# Destroy
@collections.route('/<id>', methods=['Delete'])
@login_required
def delete_collection(id):
	try:
		collection = models.Collection.get_by_id(id)

		if current_user == collection.user_id:
			collection.delete_instance(recursive=True)

			return jsonify(
		        data={}, 
		        message=f"Deleted collection with id: {id}",
		        status=200
	      	), 200
		else:
			return jsonify(
				data={},
				message="This collection belongs to a different user.",
				status=403
				),403
	
	except Exception as e:
		raise e

# Update
@collections.route('/<id>', methods=['PUT'])
@login_required
def update_collection(id):
	payload = request.get_json()
	collection = models.Collection.get_by_id(id)

	if current_user == collection.user_id:
		collection.name = payload['name'] if 'name' in payload else None
		collection.description = payload['description'] if 'description' in payload else None
		collection.category = payload['category'] if 'category' in payload else None

		collection.save()

		collection_dict = model_to_dict(collection)

		return jsonify(
			data=collection_dict,
			message=f'Updated collection: {collection.id}',
			status=200
		), 200	

	else:
		return jsonify(
			data={},
			message="This collection belongs to a different user.",
			status=403
			),403

	