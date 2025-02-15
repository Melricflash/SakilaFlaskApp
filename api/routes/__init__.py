from flask import Blueprint

from api.routes.actors import actors_router
from api.routes.films import films_router
from api.routes.match import match_router

# Create a routes module to be registered in our app
routes = Blueprint('api', __name__, url_prefix='/api')

# Register our nested routes
routes.register_blueprint(actors_router)
routes.register_blueprint(films_router)
routes.register_blueprint(match_router)