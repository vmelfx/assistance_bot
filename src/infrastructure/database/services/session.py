from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker
from src.settings import DATABASE_URL

engine: Engine = create_engine(DATABASE_URL)


def get_session(engine: Engine | None = engine) -> Session:
    Session: sessionmaker = sessionmaker(
        engine,
        expire_on_commit=False,
        autoflush=False,
    )
    return Session()
