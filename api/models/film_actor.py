from api.models import db

film_actor = db.Table('film_actor',
    db.Column('actor_id', db.Integer, db.ForeignKey('actor.actor_id')),
    db.Column('film_id', db.Integer, db.ForeignKey('film.film_id'))
)