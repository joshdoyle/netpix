import models
from flask import Blueprint

shows = Blueprint('shows', 'shows')

print('TELLY: in app.py')

@shows.route('/')
def shows_index():
	print('TELLY: in show route')
	return "in show index"