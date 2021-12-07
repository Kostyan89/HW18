from dao.model.movie import Movie


class MovieService:
    def __init__(self, movie_dao):
        self.movie_dao = movie_dao

    def get_one(self, did):
        self.movie_dao.get_one(did)

    def get_all(self):
        self.movie_dao.get_all()

    def create(self, movie_d):
        self.movie_dao.create(movie_d=movie_d)

    def delete(self, did):
        self.movie_dao.delete(did=did)

    def update(self, movie_d):
        movie = Movie(**movie_d)
        self.movie_dao.update(movie=movie)

    def partially_update(self, movie_d):
        movie = self.get_one(movie_d.get("id"))
        if "name" in movie_d:
            movie.name = movie_d.get("name")
        self.movie_dao.update(movie)

    def get_movies_by_director(self, did):
        self.movie_dao.get_movie_by_dir(did)
