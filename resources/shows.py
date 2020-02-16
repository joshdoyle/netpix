import config, models
import requests
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
# Note: 'request' is from flask; 'requests' is from Request: HTTP for Humans

shows = Blueprint('shows', 'shows')

########## Routes ############

# Index
# @shows.route('/', methods=['GET'])
# def shows_index():
# 	try:
	

# 	except Exception as e:
# 		raise e


# Show
@shows.route('/<id>', methods=['GET'])	
def get_show(id):
	try:
		show = models.Show.get_by_id(id)
		show_dict = model_to_dict(show)

		return jsonify(
			data=show_dict,
			message=f"Found show with id: {show.id}.",
			status=200
		), 200
	except Exception as e:
		raise e


# Create
@shows.route('/', methods=['POST'])
def create_show():
	try:
		payload = request.get_json()
		print(payload)

		show = models.Show.create(
			name = payload['name'],
			description = payload['description'],
			category = payload['category']
		)
		show_dict = model_to_dict(show)

		return jsonify(
			data=show_dict,
			status={'message': 'Created show'}
		), 201

	except Exception as e:
		raise e

# Destroy
@shows.route('/<id>', methods=['Delete'])
def delete_show(id):
	# TODO 2/15/20, 4:24 PM :Add logic to only let user delete their shows
	try:
		show = models.Show.get_by_id(id)
		show.delete_instance()

		return jsonify(
	        data={}, 
	        message=f"Deleted show with id: {id}",
	        status=200
      	), 200
	
	except Exception as e:
		raise e

# Update
@shows.route('/<id>', methods=['PUT'])
def update_show(id):
	payload = request.get_json()

	show = models.Show.get_by_id(id)
	show.name = payload['name'] if 'name' in payload else None
	show.description = payload['description'] if 'description' in payload else None
	show.category = payload['category'] if 'category' in payload else None

	show.save()

	show_dict = model_to_dict(show)

	return jsonify(
		data=show_dict,
		message=f'Updated show with id: {show.id}',
		status=200
	), 200	
	