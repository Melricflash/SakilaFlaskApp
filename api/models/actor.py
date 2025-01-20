from api.models import db

# Model of the actor table
class Actor(db.Model):
    actor_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255), nullable = False)
    last_name = db.Column(db.String(255), nullable = False)