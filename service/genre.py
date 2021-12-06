from dao.model.genre import Genre


class GenreService:
    def __init__(self, genre_dao):
        self.genre_dao = genre_dao

    def get_one(self, did):
        self.genre_dao.get_one(did)

    def get_all(self):
        self.genre_dao.get_all()

    def create(self, genre_d):
        self.genre_dao.create(genre_d=genre_d)

    def delete(self, did):
        self.genre_dao.delete(did=did)

    def update(self, genre_d):
        genre = Genre(**genre_d)
        self.genre_dao.update(genre=genre)

    def partially_update(self, genre_d):
        genre = self.get_one(genre_d.get("id"))
        if "name" in genre_d:
            genre.name = genre_d.get("name")
        self.genre_dao.update(genre)
