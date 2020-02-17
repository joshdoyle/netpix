import config, models
import requests
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
# Note: 'request' is from flask; 'requests' is from Request: HTTP for Humans

shows = Blueprint('shows', 'shows')

########## Routes ############

# Index
@shows.route('/', methods=['GET'])
def shows_index():
	try:
		shows = models.Show.select()
		shows_dict = [model_to_dict(s, backrefs=True) for s in shows]

		return jsonify(
			data=shows_dict,
			message=f"Retrieved {len(shows_dict)} shows.",
			status=200
		), 200
	except Exception as e:
		raise e

# Show
@shows.route('/<id>', methods=['GET'])	
def get_show(id):
	try:
		show = models.Show.get_by_id(id)
		# print('here are the shows collections', show.showcollections.collections)
		show_dict = model_to_dict(show, backrefs=True)

		return jsonify(
			data=show_dict,
			message=f"Found show with id: {show.id}.",
			status=200
		), 200
	except Exception as e:
		raise e






	