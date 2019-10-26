import random
import string

from app.db import Base
from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.types import String


class Chatroom(Base):

    __tablename__ = 'Chatroom'

    url = Column(String, unique=True)
    messages = relationship(
        'Message', back_populates='chatroom', order_by='Message.created_at'
    )

    def __init__(self):
        self.url = self.random_str(10)

    def random_str(self, length=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def to_json(self):
        """
        resp info
        1. 유저들 정보
        2. messages order by created_at asc
        """

        return {
            'url': self.url,
            'users': [],
            'messages': [m.to_json() for m in self.messages],
        }
