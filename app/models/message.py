from app.db import Base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String


class Message(Base):
    __tablename__ = 'Message'

    text = Column(String)

    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship('User', back_populates='messages')

    chatroom_id = Column(Integer, ForeignKey('Chatroom.id'))
    chatroom = relationship('Chatroom', back_populates='messages')

    def to_json(self):
        """
        resp info
         - username
         - text
         - created_at
        """
        return {'text': self.text, 'created_at': str(self.created_at)}
