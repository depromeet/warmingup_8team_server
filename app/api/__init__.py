# flake8: noqa
# isort:skip_file
import json

from typing import Any
from app import app
from app.decorators import router
from flask_socketio import SocketIO, send
from flask_cors import CORS

route: Any = router(app)
socket_io = SocketIO(app, host='0.0.0.0', port=5000, cors_allowed_origins="*")

from app.api.user import *
from app.api.chat import *
from app.api.question import *


@socket_io.on("message")
def request(data):
    message = data.get('message', '')
    # send({}, broadcast=True)
    # to_client = dict()
    # if message == 'new_connect':
    #     to_client['message'] = "새로운 유저가 난입하였다!!"
    #     to_client['type'] = 'connect'
    # else:
    #     to_client['message'] = message
    #     to_client['type'] = 'normal'
    # # emit("response", {'data': message['data'], 'username': session['username']}, broadcast=True)
    # send(to_client, broadcast=True)
