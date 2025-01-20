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
    actors = Actor.query.all() # Querying the database
    return actors_schema.dump(actors)

# Paged version of the same thing
@actors_router.get('/page/<int:page>')
def read_actors_page(page = 1):
    recordsPerPage = 50
    actors = Actor.query.paginate(page = page, per_page = recordsPerPage, error_out = False).items

    # Typically you would send this data to the template to render nicely, but I cba
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

# Deletes an actor from the DB based on their ID
@actors_router.route('/delete/<actorID>', methods = ['DELETE'])
def delete_actor(actorID):
    # Search for the actor in the actor table via ID
    actor = Actor.query.filter_by(actor_id = actorID)

    if not actor:
        return jsonify({'message': 'Actor Not Found'}), 404

    # Delete the actor
    actor.delete()
    # Commit to DB
    db.session.commit()
    return jsonify({'message': f'Deleted Actor with ID: {actorID}'}), 200

# Updates an actor from the DB using their ID
@actors_router.patch('/update/<actorID>')
def update_actor(actorID):
    actor_data = request.json # Get the parsed request body
    # Search for the actor using their ID, use first() to get the actual record rather than result
    actor = Actor.query.filter_by(actor_id=actorID).first()

    if actor:
        # Update the records according to the JSON fields
        actor.first_name = actor_data['first_name']
        actor.last_name = actor_data['last_name']
        # Update the database
        db.session.commit()
        return jsonify({'message': 'Actor Updated Successfully'}), 200

    else:
        return jsonify({'message': 'Actor Not Found'}), 404
