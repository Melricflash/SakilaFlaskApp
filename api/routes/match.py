from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from api.models import db

from api.models.actor import Actor
from api.schemas.actor import actors_schema, actor_schema

from api.models.film import Film
from api.schemas.film import film_schema, films_schema

# Create a blueprint
match_router = Blueprint('match', __name__, url_prefix='/match')


# Function to find all films for a given actor
@match_router.get('/actor/<actorID>')
def match_actor(actorID):
    # Get the actor in question
    actor = Actor.query.filter_by(actor_id = actorID).first()

    if not actor:
        return jsonify({'message': 'Actor Not Found'}), 404

    # Use the association table to retrieve all films with the actor in it
    films = actor.films
    # Dump out to the schema and return to user
    return films_schema.dump(films)

@match_router.get('/film/<filmID>')
def match_film(filmID):
    # Get the film record in question
    film = Film.query.filter_by(film_id = filmID).first()

    if not film:
        return jsonify({'message': 'Film Not Found'}), 404

    # Use the association table to retrieve all actors in the film
    actors = film.actors
    # Return to user
    return actors_schema.dump(actors)