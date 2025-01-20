from api.models import db

# Model of the film table
class Film(db.Model):
    film_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(128), nullable = False)
    description = db.Column(db.Text, nullable = True)
    release_year = db.Column(db.Integer, nullable = False)