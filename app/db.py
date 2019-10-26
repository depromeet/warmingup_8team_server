from datetime import datetime
from typing import Any

from app.config import Config
from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = Config.engine()
create_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)


class BaseModel:
    id = Column(Integer, primary_key=True)

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    @property
    def session(self):
        return create_session().object_session(self)

    @property
    def query(self):
        return self.session.query(self.__class__)


Base: Any = declarative_base(bind=engine, cls=BaseModel)
