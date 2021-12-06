from flask import request
from flask_restx import Namespace, Resource

from dao.movie import MovieSchema
from implemented import movie_service


movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        all_movies = movie_service.get_all()
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        movie_service.create(req_json)
        return "", 201

@movie_ns.route('/<int:uid>')
class MovieView(Resource):
    def get(self, uid: int):
        movie = movie_service.get_one(uid)
        return movie_schema.dump(movie), 200

    def put(self, uid: int):
        req_json = request.json
        movie_service.filter_by(uid).update(req_json)
        return "", 204

    def delete(self, uid: int):
        movie_service.delete(uid)
        return "", 204

    def patch(self, uid: int):
        req_json = request.json
        movie_service.filter_by(uid).partially_update(req_json)
        return "", 204

    def get_by_director(self, director_id: int):
        return movie_service.get_by_director(director_id), 200