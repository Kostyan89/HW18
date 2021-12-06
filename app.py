from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    return app


def register_extensions(app):
    db.init_app(app=app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


cfg = Config()
app = create_app(config=cfg)
register_extensions(app=app)

# функция
# def create_data(app, db):
#     with app.app_context():
#         db.create_all()
#
#         создать несколько сущностей чтобы добавить их в БД
#
#         with db.session.begin():
#             db.session.add_all(здесь список созданных объектов)
#
#
#
# if __name__ == '__main__':
#     app.run(host="localhost", port=10001, debug=True)
