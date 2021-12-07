from marshmallow import Schema, fields

from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        return self.session.query(Movie).all()

    def create(self, movie_d):
        ent = Movie(**movie_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    def delete(self, gid):
        movie = self.get_one(gid=gid)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_d):
        movie = self.get_one(movie_d.get("id"))
        movie.name = movie_d.get("name")
        self.session.add(movie)
        self.session.commit()

    def get_movie_by_dir(self, director_id):
        self.session.query(Movie).filter_by(director_id).get_all()



class MovieSchema(Schema):
    id = fields.Int()
    title =fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()