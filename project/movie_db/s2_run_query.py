# -*- coding: utf-8 -*-

"""
.. note::

    session + text sql doesn't work.
"""

from sqlalchemy import text
from sqlalchemy_mate import engine_creator

from learn_datasette.datamodel import Movie
from s1_make_data import db_file

engine = engine_creator.create_sqlite(db_file)

sql = text("""
SELECT * 
FROM movie
WHERE rowid in 
(
    SELECT rowid 
    FROM movie_fts 
    WHERE movie_fts 
    MATCH 'man'
) 
ORDER BY id 
LIMIT 101
""")
movie_columns = [c.name for c in Movie.__table__._columns]
for row in engine.execute(sql):
    movie = Movie(**dict(zip(movie_columns, row)))
    print(movie)
