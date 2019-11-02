# flake8: noqa
from app.db import Base
from app.models.bot import Bot
from app.models.chatroom import Chatroom
from app.models.message import Message
from app.models.question import Question
from app.models.user import User
from sqlalchemy import Column
from sqlalchemy.types import JSON


class Packet(Base):
    __tablename__ = "Packet"

    request_header = Column(JSON)
    request_body = Column(JSON)

    response_header = Column(JSON)
    response_body = Column(JSON)
