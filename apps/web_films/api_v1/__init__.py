from flask import request, Blueprint
from flask_restful import Api
from .resourses import FilmListResource, FilmResource, LoginApi

web_films = Blueprint('films_v1_0_bp', __name__)
api = Api(web_films)


api.add_resource(FilmListResource, '/api/v1/films/', endpoint='film_list_resource')
api.add_resource(FilmResource, '/api/v1/films/<int:film_id>', endpoint='film_resource')
api.add_resource(LoginApi, '/api/v1/login', endpoint='film_login')