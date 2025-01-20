from api.models import db
from api.models.film_actor import film_actor
from api.models.film import Film # Genuinely this one missing import destroys everything

# Model of the actor table
class Actor(db.Model):
    actor_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255), nullable = False)
    last_name = db.Column(db.String(255), nullable = False)

    # Association to films, we can access this later with the back_populates name
    films = db.relationship('Film', secondary = film_actor, back_populates = 'actors')