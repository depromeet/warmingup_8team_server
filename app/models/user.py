from app.db import Base
from app.models import Chatroom, Message
from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import backref, relationship
from sqlalchemy.types import Boolean, Integer, String


class User(Base):
    __tablename__ = 'User'

    email = Column(String, unique=True)
    name = Column(String)

    chatroom_id = Column(Integer, ForeignKey('Chatroom.id'))
    chatroom: Chatroom = relationship('Chatroom', backref=backref('users'))

    messages = relationship('Message', back_populates='user')

    profile_url = Column(String)
    thumbnail_url = Column(String)

    gender = Column(Boolean)

    def __init__(self, profile: dict):
        self.update(profile)

    def send_message(self, text) -> Message:
        message = Message(
            text=text, user_id=self.id, chatroom_id=self.chatroom_id
        )
        self.session.add(message)
        self.session.flush()

        return message

    def update(self, profile: dict):
        self.name = profile['profile']['nickname']
        self.profile_url = profile['profile']['profile_image_url']
        self.thumbnail_url = profile['profile']['thumbnail_image_url']
        self.email = profile['email']
        self.gender = profile['gender'] == 'male'

    def to_json(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'thumbnail_url': self.thumbnail_url,
            'profile_url': self.profile_url,
            'email': self.email,
            'gender': self.gender,
            'chatroom': self.chatroom.to_json(),
        }
