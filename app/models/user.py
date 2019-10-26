from app.db import Base
from app.models import Message
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import backref, relationship
from sqlalchemy.types import Integer, String


class User(Base):
    __tablename__ = 'User'

    email = Column(String, unique=True)
    name = Column(String)

    chatroom_id = Column(Integer, ForeignKey('Chatroom.id'))
    chatroom = relationship('Chatroom', backref=backref('users'))

    messages = relationship('Message', back_populates='user')

    def send_message(self, text) -> Message:
        message = Message(
            text=text, user_id=self.id, chatroom_id=self.chatroom_id
        )
        self.session.add(message)
        self.session.flush()

        return message
