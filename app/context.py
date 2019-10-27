from typing import Any, Union

from app.models import Base, User
from flask import session as mem_session
from sqlalchemy.orm import scoped_session


class ApiContext:

    session: scoped_session
    request = None
    data: dict = {}
    user: Union[User, Any]

    def __init__(self, session: scoped_session, request):
        self.session = session
        self.request = request
        self.user = None

        if self.request.method == 'POST':
            self.data = self.request.json
        elif self.request.method == 'GET':
            self.data = self.request.args

        if 'user_id' in mem_session:
            self.user = (
                self.session.query(User)
                .filter(User.id == mem_session['user_id'])
                .first()
            )

    def query(self, model: Base):
        return self.session.query(model)
