from app.db import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String


class Question(Base):

    __tablename__ = 'Question'

    message = Column(String)
    answer = Column(String)

    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship('User', back_populates='questions')

    def to_json(self):
        return {'id': self.id, 'message': self.message, 'answer': self.answer}
