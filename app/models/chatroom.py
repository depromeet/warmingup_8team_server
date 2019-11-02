import random
import string

from app.db import Base
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.types import String


class Chatroom(Base):

    __tablename__ = 'Chatroom'

    name = Column(String)
    thumbnail = Column(String)

    url = Column(String, unique=True)
    messages = relationship(
        'Message', back_populates='chatroom', order_by='Message.created_at'
    )

    bot = relationship('Bot', uselist=False, back_populates='chatroom')

    def __init__(self):
        self.url = self.random_str(10)

    def random_str(self, length=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def to_json(self):
        users = self.users

        data = []
        for u in users:
            data.append(
                {
                    'name': u.name,
                    'thumbnail_url': u.thumbnail_url,
                    'email': u.email,
                    'gender': u.gender,
                }
            )

        return {
            'url': self.url,
            'users': data,
            'thumbnail': self.thumbnail,
            'name': self.name,
            'messages': [m.to_json() for m in self.messages],
        }
