from app.db import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import backref, relationship
from sqlalchemy.types import Integer, String


class User(Base):
    __tablename__ = 'User'

    email = Column(String, unique=True)
    name = Column(String)

    chatroom_id = Column(Integer, ForeignKey('Chatroom.id'))
    chatroom = relationship('Chatroom', backref=backref('users'))
