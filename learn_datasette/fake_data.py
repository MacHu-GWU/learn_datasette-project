# -*- coding: utf-8 -*-

import random
from faker import Faker
from .datamodel import Movie, Genre, Maker

fake = Faker()

n_movie = 500
n_genre = 30
n_maker = 10

makers = [
    Maker(id=id, name="{} {}".format(fake.company(), fake.company_suffix()))
    for id in range(1, 1 + n_maker)
]

genre_set = set([fake.word() for _ in range(100)])
genre_list = list(genre_set)
genre_list.sort()
genres = [
    Genre(id=id, name=name)
    for id, name in zip(range(1, 1 + n_genre), genre_list[:n_genre])
]

movies = [
    Movie(
        id=id,
        title=fake.sentence(),
        year=random.randint(1950, 2018),
        maker=random.choice(makers),
        genres=random.sample(genres, random.randint(2, 5)),
    )
    for id in range(1, 1 + n_movie)
]
