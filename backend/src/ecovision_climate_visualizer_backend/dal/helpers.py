import os
from sqlalchemy import create_engine
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from .models import Base

def get_engine(db_url:str):
    connect_args = {"check_same_thread": False}
    engine = create_engine(db_url, connect_args=connect_args)
    return engine

def create_tables(engine: Engine):
    Base.metadata.create_all(engine)


