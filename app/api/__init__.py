# flake8: noqa
# isort:skip_file
import json

from typing import Any
from app import app
from app.decorators import router, create_context
from flask_socketio import SocketIO, send, emit
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
    send(send_message.to_json(), broadcast=True)

    # send({}, broadcast=True)
    # to_client = dict()
    # if message == 'new_connect':
    #     to_client['message'] = "새로운 유저가 난입하였다!!"
    #     to_client['type'] = 'connect'
    # else:
    #     to_client['message'] = message
    #     to_client['type'] = 'normal'
    # emit("response", {'data': message['data'], 'username': session['username']}, broadcast=True)
    # send(to_client, broadcast=True)
