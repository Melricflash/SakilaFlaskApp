from api.models.film import Film
from api.schemas import ma

# Autogenerate a schema for the Film model
class FilmSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Film

# Instantiate the schema for both a single film and many films
film_schema = FilmSchema()
films_schema = FilmSchema(many = True)