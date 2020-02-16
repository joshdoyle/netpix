import config, models
import requests
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
# https://api.themoviedb.org/3/search/multi?api_key=8092585d243569d68c08aeb452c21fc6&language=en-US&query=test&page=1&include_adult=false
# images: https://image.tmdb.org/t/p/w500/kqjL17yufvn9OVLyXYpvtyrFfak.jpg
		query = request.args.get('query')
		print('this is the query from the query string', query)

		payload = {
			'api_key': config.TMDB_API_KEY, 
			'language': 'en-US',
			'query': query,
			'page': '1',
			'include_adult': 'false'
		}

		r = requests.get('https://api.themoviedb.org/3/search/multi?', params=payload)
		print(r.url)

		return jsonify(
			data=r.text,
			message=f"Retrieved data from TMDB.",
			status=200
		), 200

	except Exception as e:
		raise e
