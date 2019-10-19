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

    """def to_json(self):
    # TODO: 자신의 column들을 탐색해 전부 JSON으로 변환 및 반환
    data = {}
    for column in self.__table__.columns:
      attr = getattr(self, column.key)
      print(type(attr))
      if type(attr) is datetime:
        attr = int(attr.timestamp() * 1000)
      data[column.key] = attr

    return data"""


Base: Any = declarative_base(bind=engine, cls=BaseModel)
