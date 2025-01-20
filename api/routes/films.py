from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from api.models import db
from api.models.film import Film
from api.schemas.film import film_schema, films_schema

# Create the blueprint and insert into app.py
films_router = Blueprint('films', __name__, url_prefix='/films')

# GET Requests all films in the database
@films_router.get('/')
def read_all_films():
    films = Film.query.all() # Query the database
    return films_schema.dump(films)