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


@route('/', methods=['GET'])
def index(context: ApiContext):
    return {
        'kkirook': 'hi'
    }


@socket_io.on('connect')
def connect():
    context: ApiContext = create_context()
    print(context.session)
    join_room(context.user.chatroom.url)
    print('join')


@socket_io.on("message")
def request(data):
    context: ApiContext = create_context()
    chatroom = context.user.chatroom
    chatroom_users = chatroom.users

    message = data.get('message', '')

    send_message = context.user.send_message(message)
    send(send_message.to_json(), broadcast=True, room=chatroom.url)
    context.session.commit()
