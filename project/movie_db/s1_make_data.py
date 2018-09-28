# -*- coding: utf-8 -*-

import os
from pathlib_mate import Path
from sqlalchemy import text
from learn_datasette.fake_data import movies
from learn_datasette.datamodel import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_mate import engine_creator

db_file = Path(__file__).change(new_basename="movie.sqlite").abspath


def make_data(engine):
    ses = sessionmaker(bind=engine)()
    ses.add_all(movies)
    ses.commit()
    ses.close()

    # create full text search virtual table
    sql = text("""
    CREATE VIRTUAL TABLE "movie_fts" USING FTS4 (
        title,
        maker_name,
        content="movie"
    );
    """)
    engine.execute(sql)

    # define mapping, create index
    # use built-in rowid as primary key
    sql = text("""
    INSERT INTO "movie_fts" (rowid, title, maker_name)
        SELECT movie.rowid, movie.title, maker.name
        FROM movie JOIN maker ON movie.maker_id = maker.id;
    """)
    engine.execute(sql)


if __name__ == "__main__":
    if os.path.exists(db_file):
        os.remove(db_file)
    engine = engine_creator.create_sqlite(db_file)
    Base.metadata.create_all(engine)
    make_data(engine)
