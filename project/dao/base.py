from sqlalchemy.orm import scoped_session


class BaseDao:

    def __init__(self, session: scoped_session):
        self._db_session = session

