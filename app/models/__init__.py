from sqlalchemy.types import JSON
from sqlalchemy import Column

from app.db import Base


class Packet(Base):
    __tablename__ = 'Packet'


    request_header = Column(JSON)
    request_body = Column(JSON)

    response_header = Column(JSON)
    response_body = Column(JSON)
