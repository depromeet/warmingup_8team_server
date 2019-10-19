from app.db import Base
from sqlalchemy import Column
from sqlalchemy.types import String


class User(Base):

    email = Column(String, unique=True)
