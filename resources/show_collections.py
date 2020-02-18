import models
from models import ShowCollection, Show
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
from flask_login import current_user, login_required

show_collections = Blueprint('show_collections', 'show_collections')

########## Routes ############

# Index
# I DON'T THINK WE NEED THIS INDEX
# @show_collections.route('/', methods=['GET'])
# def show_collections_index():
# 	try:
# 		show_collections = models.ShowCollection.select()
# 		show_collections_dicts = [model_to_dict(c) for c in show_collections]

# 		return jsonify(
# 			data=show_collections_dicts,
# 			message=f"Retrieved {len(show_collections_dicts)} show_collections.",
# 			status=200
# 		), 200
# 	except Exception as e:
# 		raise e

# Show
@show_collections.route('/<id>', methods=['GET'])	
def get_show_collection(id):
	try:
		show_collection_dict = {
			"collection_id": id,
			"records_returned": 0,
			"shows": []
		}
	
		shows = \
			Show.select(ShowCollection, Show) \
			.join(ShowCollection) \
			.where(ShowCollection.collection_id == id)		

		i = 0
		for s in shows:
			print('line 44 in show for loop')
			i += 1
			show_dict = model_to_dict(s)
			show_dict['user_description'] = s.showcollection.user_description
			# show_dict['user'] = s.showcollection.user_id
			show_collection_dict['shows'].append(show_dict)


			show_collection_dict['records_returned'] = i

		return jsonify(
			data=show_collection_dict,
			status={'message': 'Retrieved show_collection'}
		), 201

	except models.DoesNotExist:
		return jsonify(
			message=f"Collection: {id} does not exist.",
			status=204
		), 204


# Create
@show_collections.route('/', methods=['POST'])
@login_required
def create_show_collection():
	try:
		payload = request.get_json()
		print(payload)

		# loop the show collections
		for s in payload['shows']:
			# first find or add the show
			try:
				show = models.Show.get(Show.tmdb_id == s['tmdb_id'])
			except Show.DoesNotExist:
				show = models.Show.create(
					tmdb_id = s['tmdb_id'],
					tmdb_title = s['tmdb_title'],
					tmdb_poster_path = s['tmdb_poster_path'],
					tmdb_backdrop_path = s['tmdb_backdrop_path'],
					tmdb_media_type = s['tmdb_media_type'],
					tmdb_overview = s['tmdb_overview']
				)
		
			# now relate the show to the collection
			show_collection = models.ShowCollection.create(
				collection_id = payload['collection_id'],
				show_id = show.id,
				user_description = s['user_description'],
				order = s['order'],
				user_id = current_user.id
			)

		show_collection_dict = model_to_dict(show_collection)

		return jsonify(
			data=show_collection_dict,
			status={'message': 'Created show_collection'}
		), 201

	except Exception as e:
		raise e

# Destroy
@show_collections.route('/<id>', methods=['Delete'])
@login_required
def delete_show_collection(id):
	# TODO 2/15/20, 4:24 PM :Add logic to only let user delete their show_collections
	try:
		show_collection = models.ShowCollection.get_by_id(id)
		if current_user == show_collection.user_id:
			show_collection.delete_instance()

			return jsonify(
		        data={}, 
		        message=f"Deleted show_collection with id: {id}",
		        status=200
	      	), 200

		else:
			return jsonify(
				data={},
				message="This show_collection belongs to a different user.",
				status=403
				),403      		
			
	except Exception as e:
		raise e

# Update
@show_collections.route('/<id>', methods=['PUT'])
@login_required
def update_show_collection(id):
	payload = request.get_json()
	show_collection = models.ShowCollection.get_by_id(id)

	if current_user == show_collection.user_id:
		show_collection.user_description = payload['user_description'] if 'user_description' in payload else None
		show_collection.order = payload['order'] if 'order' in payload else None
		show_collection.save()
		show_collection_dict = model_to_dict(show_collection)

		return jsonify(
			data=show_collection_dict,
			message=f'Updated show_collection with id: {show_collection.id}',
			status=200
		), 200	
	
	else:
		return jsonify(
			data={},
			message="This show_collection belongs to a different user.",
			status=403
			),403

######### Private Functions #########

# # Get a single instance of Show Collection and shows. Needed by Show_Collection and Create_Collection
# def __get_show_collection(id):

# 	show_collection_dict = {
# 		"collection_id": id,
# 		"records_returned": 0,
# 		"shows": []
# 	}
	
# 	shows = \
# 		Show.select(ShowCollection, Show) \
# 		.join(ShowCollection) \
# 		.where(ShowCollection.collection_id == id)		

# 	i = 0
# 	for s in shows:
# 		i += 1
# 		show_dict = model_to_dict(s)
# 		show_dict['user_description'] = s.showcollection.user_description
# 		show_dict['user'] = s.showcollection.user
# 		show_collection_dict['shows'].append(show_dict)

# 	show_collection_dict['records_returned'] = i

# 	return show_collection_dict

