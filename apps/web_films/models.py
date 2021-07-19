
from apps.db import BaseModelMixin, db

from sqlalchemy import Integer, String, Column, ForeignKey

from sqlalchemy.orm import relationship


class Film(db.Model, BaseModelMixin):
    id = Column(Integer, primary_key=True)
    title = Column(String)
    length = Column(Integer)
    year = Column(Integer)
    director = Column(String)
    actors = relationship('Actor', backref='film', lazy=False, cascade='all, delete-orphan')

    def __init__(self, title, length, year, director, actors=[]):
        self.title = title
        self.length = length
        self.year = year
        self.director = director
        self.actors = actors
    def __repr__(self):
        return f'Film({self.title})'
    def __str__(self):
        return f'{self.title}'

class Actor(db.Model, BaseModelMixin):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    film_id = Column(Integer, ForeignKey('film.id'), nullable=False)

    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return f'Actor({self.name})'
    def __str__(self):
        return f'{self.name}'