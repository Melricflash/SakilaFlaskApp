from api.models import db
from api.models.film_actor import film_actor

# Model of the film table
class Film(db.Model):
    film_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(128), nullable = False)
    description = db.Column(db.Text, nullable = True)
    release_year = db.Column(db.Integer, nullable = False)
    language_id = db.Column(db.Integer, nullable = False)
    original_language_id = db.Column(db.Integer, nullable = True)

    # Association to Actors
    actors = db.relationship('Actor', secondary = film_actor, back_populates = 'films')
