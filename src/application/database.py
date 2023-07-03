from functools import wraps

from sqlalchemy.orm import Session
from src.infrastructure.database.services.session import get_session
from src.infrastructure.errors import DatabaseError


def transaction(func):
    """
    This decorator should be used with all handlers
    that want's to run all requests within one transaction
    """

    @wraps(func)
    def inner(*args, **kwargs):
        session: Session = get_session()
        try:
            result = func(session, *args, **kwargs)
            session.commit()
            return result
        except DatabaseError as error:
            print(error)
            session.rollback()
            raise DatabaseError
        finally:
            session.close()

    return inner
