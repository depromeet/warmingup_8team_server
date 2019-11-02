# flake8: noqa
# isort:skip_file
import json

from typing import Any
from app import app
from app.decorators import router, create_context
from flask_socketio import SocketIO, send, emit, join_room
from flask_cors import CORS

route: Any = router(app)
socket_io = SocketIO(app, host='0.0.0.0', port=5000, cors_allowed_origins="*")

from app import models
from app.context import ApiContext
from app.api.user import *
from app.api.chat import *
from app.api.question import *
from flask import session


@socket_io.on("message")
def request(data):
    context: ApiContext = create_context()
    chatroom = context.user.chatroom
    chatroom_users = chatroom.users

    message = data.get('message', '')
    
    send_message = context.user.send_message(message)
    context.session.commit()
    join_room(chatroom.url)
    send(
        send_message.to_json(),
        broadcast=True,
        room=chatroom.url
    )
