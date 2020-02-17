import models

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user, current_user, logout_user
from playhouse.shortcuts import model_to_dict

users = Blueprint('users', 'users')

@users.route('/register', methods=['POST'])
def register():
	payload = request.get_json()
	payload['email'] = payload['email'].lower()
	payload['username'] = payload['username'].lower()

	try:
	    models.User.get(models.User.email == payload['email'])

	    return jsonify(
	    	data={},
	    	message='A user with that email already exists.',
	    	status=401
	    ), 401	

	except models.User.DoesNotExist:

		created_user = models.User.create(
			username=payload['username'],
			email=payload['email'],
			password=generate_password_hash(payload['password'])
		)

		login_user(created_user)
		user_dict = model_to_dict(created_user)
		user_dict.pop('password')

		return jsonify(
			data=user_dict,
			message=f"Registered {user_dict['email']}",
			status=201
		), 201

@users.route('/login', methods=['POST'])
def login():
	payload = request.get_json()
	payload['email'] = payload['email'].lower()
	# payload['username'] = payload['username'].lower() 

	try:
  		user = models.User.get(models.User.email == payload['email'])
  		user_dict = model_to_dict(user)
  		user_authenticated = check_password_hash(user_dict['password'], payload['password'])
  		if user_authenticated:
  			login_user(user)
  			user_dict.pop('password')

  			return jsonify(
  				data=user_dict,
  				message=f"Logged in {user_dict['email']}.",
  				status=200
  			), 200

  		else:
  			return jsonify(
  				data={},
  				message="Email or password is incorrect",
  				status=401
  				), 401
  			
	except models.User.DoesNotExist:
  		return jsonify(
  			data={},
  			message="Email or password is incorrect",
  			status=401
  			), 401

@users.route('/logout', methods=['GET'])
def logout():
	logout_user()
	return jsonify(
		data={},
		message="Logged out.",
		status=200
	), 200