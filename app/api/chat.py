import os

from app import app, models
from app.api import route
from app.context import ApiContext


@route('/chatroom', methods=['GET'])
def get_chatroom(context: ApiContext) -> dict:
    chatroom: models.Chatroom = context.user.chatroom

    return {
        'url': chatroom.url,
        'messages': [m.to_json() for m in chatroom.messages],
    }


@route('/chatroom/<url>', methods=['POST'])
def update_chatroom(context: ApiContext, url) -> dict:
    """
    thumbnail
    name
    """
    if context.user.chatroom.url != url:
        raise
    name = context.request.form['name']
    thumbnail = context.request.files['thumbnail']
    thumbnail.filename = (
        f"{context.user.chatroom.random_str()}"
        f".{thumbnail.filename.split('.')[-1]}"
    )
    # TODO(clogic): File을 다운로드해서 static folder에 저장해두기
    # TODO(clogic): EC2에 띄울거면 s3에 저장하는것도 생각하기

    thumbnail.save(
        os.path.join(app.config['UPLOAD_FOLDER'], thumbnail.filename)
    )

    context.user.chatroom.name = name
    context.user.chatroom.thumbnail = thumbnail.filename
    return context.user.chatroom.to_json()


@route('/message', methods=['POST'])
def send_message(context: ApiContext) -> dict:
    """
    req params:
        - text: str
    """
    m = context.user.send_message(context.data['text'])

    return m.to_json()
