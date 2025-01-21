from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from api.models import db
from api.models.film import Film
from api.schemas.actor import actor_schema
from api.schemas.film import film_schema, films_schema

# Create the blueprint and register inside __init__
films_router = Blueprint('films', __name__, url_prefix='/films')

# GET Requests all films in the database
@films_router.get('/')
def read_all_films():
    films = Film.query.all() # Query the database
    return films_schema.dump(films)

# GET Requests a specific film in the database
@films_router.get('/<film_id>')
def read_film(film_id):
    film = Film.query.get(film_id)
    if film:
        return film_schema.dump(film), 200
    else:
        return jsonify({'message': 'Film Not Found'}), 404

# Function to create a new film and insert into the database
@films_router.post('/')
def create_film():
    # Retrieve the data using a json request
    film_data = request.json
    # Check to see if the JSON data is valid
    try:
        film_schema.load(film_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create a new Film model
    film = Film(**film_data)
    # Insert Record
    db.session.add(film)
    # Update the database
    db.session.commit()

    return film_schema.dump(film)

# Delete a specific film from the database using the ID
@films_router.route('/delete/<filmID>', methods = ['DELETE'])
def delete_film(filmID):
    film = Film.query.filter_by(film_id = filmID)

    if not film:
        return jsonify({'message': 'Film Not Found'}), 404

    # Delete the film, watch out for SQL Constraints
    film.delete()
    db.session.commit()
    return jsonify({'message': f'Deleted film with ID: {filmID}'}), 200

# Update a specific film from the database using its ID
@films_router.patch('/update/<filmID>')
def update_film(filmID):
    film_data = request.json
    # Get the specific record rather than the result
    film = Film.query.filter_by(film_id = filmID).first()

    if not film:
        return jsonify({'message': 'Film Not Found'}), 404

    film.description = film_data['description']
    film.title = film_data['title']
    film.release_year = film_data['release_year']
    film.language_id = film_data['language_id']
    film.original_language_id = film_data['original_language_id']

    db.session.commit()
    return jsonify({'message': 'Film Updated Successfully'}), 200


