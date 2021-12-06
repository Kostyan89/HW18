from flask import request
from flask_restx import Namespace, Resource

from dao.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        return director_schema.dump(all_directors), 200

    def post(self):
        req_json = request.json
        director_service.create(req_json)
        return "", 201


@director_ns.route('/<int:uid>')
class DirectorView(Resource):
    def get(self, uid: int):
        director = director_service.get_one(uid)
        return director_schema.dump(director), 200

    def put(self, uid: int):
        req_json = request.json
        director_service.filter_by(uid).update(req_json)
        return "", 204

    def delete(self, uid: int):
        director_service.delete(uid)
        return "", 204

    def patch(self, uid: int):
        req_json = request.json
        director_service.filter_by(uid).partially_update(req_json)
        return "", 204