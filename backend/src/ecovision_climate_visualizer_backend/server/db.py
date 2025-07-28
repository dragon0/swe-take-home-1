from fastapi import  Depends
from sqlalchemy.orm import Session
from sqlalchemy.engine import Engine
from typing import Annotated

from ..dal.helpers import get_db_url, get_engine


DbUrlDep = Annotated[Engine, Depends(get_db_url)]

def get_engine_from_db_url(db_url: DbUrlDep):
    return get_engine(db_url)

EngineDep = Annotated[Engine, Depends(get_engine_from_db_url)]

def get_session(engine: EngineDep):
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

