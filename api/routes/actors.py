from flask import Blueprint, request, jsonify
from marshmallow import ValidationError

from api.models import db
from api.models.actor import Actor
from api.schemas.actor import actors_schema, actor_schema

# Create a "Blueprint" or module
# To be inserted into the Flask app
actors_router = Blueprint('actors', __name__, url_prefix='/actors')


# GET requests to the collection return a list of all actors in the database
@actors_router.get('/')
def read_all_actors():
    actors = Actor.query.all() # Querying the databse
    return actors_schema.dump(actors)

# GET requests o a specific document in the collection return a single actor
@actors_router.get('/<actor_id>')
def read_actor(actor_id):
    actor = Actor.query.get(actor_id)
    return actor_schema.dump(actor)

@actors_router.post('/')
def create_actor():
    actor_data = request.json # Get the parsed request body

    try:
        actor_schema.load(actor_data) # Validate the request against the schema
    except ValidationError as err:
        return jsonify(err.messages), 400

    actor = Actor(**actor_data) # Create a new actor model
    db.session.add(actor) # Insert the record
    db.session.commit() # Update the database

    return actor_schema.dump(actor) # Serialise the created actor