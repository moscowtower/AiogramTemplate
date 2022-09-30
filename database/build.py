from contextlib import suppress

import sqlalchemy.exc
import os.path
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from loader import db
import database.types as types
from sqlalchemy_utils import create_database, drop_database


def init():
    engine = db.engine
    with suppress(sqlalchemy.exc.OperationalError):
        drop_database(db.engine_string())
    create_database(db.engine_string())
    types.Base.metadata.create_all(bind=engine)


def soft_init():
    engine = db.engine
    types.Base.metadata.create_all(bind=engine)


init()
