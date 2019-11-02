from app.db import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String


class Question(Base):

    __tablename__ = 'Question'

    message = Column(String)
    answer = Column(String)

    bot_id = Column(Integer, ForeignKey('Bot.id'))
    bot = relationship('Bot', back_populates='questions')

    def to_json(self):
        return {'message': self.message, 'answer': self.answer}
