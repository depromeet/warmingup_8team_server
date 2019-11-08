# flake8: noqa
# isort:skip_file
import json
import random

from datetime import datetime, timedelta
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
    return {'kkirook': 'hi'}


@socket_io.on('connect')
def connect():
    context: ApiContext = create_context()
    join_room(context.user.chatroom.url)


@socket_io.on("message")
def request_message(data):
    # TODO(clogic): event trigger해서 bot도 메시지 보내도록 해야 함
    context: ApiContext = create_context()
    user_ids = [u.id for u in context.user.chatroom.users]
    chatroom = context.user.chatroom
    chatroom_users = chatroom.users

    message = data.get('message', '')

    send_message = context.user.send_message(message)
    send(send_message.to_json(), broadcast=True, room=chatroom.url)

    try:
        message = context.session.query(models.Message).all()[-1].created_at
        last_question = (
            context.session.query(models.Message)
            .filter(models.Message.user == None)
            .all()[-1]
            .text
        )
    except Exception:
        context.session.commit()
        return
    res = (
        context.session.query(models.Question)
        .filter(models.Question.message == last_question)
        .filter(models.Question.user_id.in_(user_ids))
        .all()
    )
    # if datetime.now() > message + timedelta(hours=3) and not res: # REAL CODE
    # if True:  # TEST
    if not res:  # TEST
        questions = []
        for u in context.user.chatroom.users:
            '''if u.id == context.user.id: # REAL_CODE
                continue'''

            questions += u.questions

        selected = random.choice(questions)
        question = models.Message(chatroom=chatroom, text=selected.message)
        context.session.add(question)
        context.session.flush()

        send(question.to_json(), broadcast=True, room=chatroom.url)
    else:

        q: models.Question = random.choice(res)

        m = models.Message(chatroom=chatroom, text=q.answer)
        context.session.add(m)
        context.session.flush()
        send(m.to_json(), broadcast=True, room=chatroom.url)

    context.session.commit()
