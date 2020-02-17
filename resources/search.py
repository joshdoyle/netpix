import config, models
import requests, json
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict
# Note: 'request' is from flask; 'requests' is from Request: HTTP for Humans

search = Blueprint('search', 'search')

########## Routes ############

# Index
@search.route('/', methods=['GET'])
def search_index():
	try:
		print('in search index')

		query = request.args.get('query')

		payload = {
			'api_key': config.TMDB_API_KEY, 
			'language': 'en-US',
			'query': query,
			'page': '1',
			'include_adult': 'false'
		}
		# todo: move url to constant
		r = requests.get('https://api.themoviedb.org/3/search/multi?', params=payload)
		response_dict = json.loads(r.text)

		data_dict = {
			"page": response_dict['page'],
			"total_results": response_dict['total_results'],
			"total_pages": response_dict['total_pages'],
			"results": [] 
		}

		for result in response_dict['results']:
			title = result['name'] if result['media_type'] == "tv" else result['title']	
			result_dict = {
				"tmdb_id": result['id'],
				"tmdb_title": title,
				"tmdb_poster_path": result['poster_path'],
				"tmdb_backdrop_path": result['backdrop_path'],
				"tmdb_media_type": result['media_type'],
				"tmdb_overview": result['overview']
			}
			data_dict['results'].append(result_dict)

		return jsonify(
			data=data_dict,
			message=f"Retrieved data from TMDB.",
			status=200
		), 200

	except Exception as e:
		raise e
