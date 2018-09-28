# -*- coding: utf-8 -*-

from sqlalchemy import Table, Column
from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy_mate import ExtendedBase

Base = declarative_base()

movie_and_genre = Table(
    "movie_and_genre", Base.metadata,
    Column("movie_id", Integer, ForeignKey("movie.id"), primary_key=True),
    Column("genre_id", Integer, ForeignKey("genre.id"), primary_key=True),
)


class Movie(Base, ExtendedBase):
    __tablename__ = "movie"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    maker_id = Column(Integer, ForeignKey("maker.id"))

    maker = relationship("Maker")
    genres = relationship("Genre", secondary=movie_and_genre, back_populates="movies")


class Genre(Base, ExtendedBase):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    movies = relationship("Movie", secondary=movie_and_genre, back_populates="genres")


class Maker(Base, ExtendedBase):
    __tablename__ = "maker"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    movies = relationship("Movie", back_populates="maker")
