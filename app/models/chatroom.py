import random
import string

from app.db import Base
from sqlalchemy import Column
from sqlalchemy.types import String


class Chatroom(Base):

    __tablename__ = 'Chatroom'

    url = Column(String, unique=True)

    def __init__(self):
        self.url = self.random_str(10)

    def random_str(self, length=10):
        """Generate a random string of fixed length """
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
