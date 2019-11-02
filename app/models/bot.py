from app.db import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer


class Bot(Base):
    """
    like user 모델
    user처럼 질문하고 답변을 받는다
    누군가가 메시지를 던지면 무작위 문제가 나감
    """

    __tablename__ = 'Bot'

    chatroom_id = Column(Integer, ForeignKey('Chatroom.id'))
    chatroom = relationship('Chatroom', back_populates='bot')

    # questions = relationship('Question', back_populates='bot')
