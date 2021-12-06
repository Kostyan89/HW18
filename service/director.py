from dao.model.director import Director


class DirectorService:
    def __init__(self, director_dao):
        self.director_dao = director_dao

    def get_one(self, did):
        self.director_dao.get_one(did)

    def get_all(self):
        self.director_dao.get_all()

    def create(self, director_d):
        self.director_dao.create(director_d=director_d)

    def delete(self, did):
        self.director_dao.delete(did=did)

    def update(self, director_d):
        director = Director(**director_d)
        self.director_dao.update(director=director)

    def partially_update(self, director_d):
        director = self.get_one(director_d.get("id"))
        if "name" in director_d:
            director.name = director_d.get("name")
        self.director_dao.update(director)
