import models
from flask import Blueprint

show_collections = Blueprint('show_collections', 'show_collections')


@show_collections.route('/', methods=['GET'])
def shows_index():
	print('TELLY: in show_collections route')
	return "in show_collections index"

# This route probably won't be part of api. Putting here for test
@show_collections.route('/', methods=['POST'])
def create_show():
	return 'in show_collections create route'