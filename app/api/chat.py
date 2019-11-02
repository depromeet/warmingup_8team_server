from app import models
from app.api import route
from app.context import ApiContext


@route('/chatroom', methods=['GET'])
def get_chatroom(context: ApiContext) -> dict:
    chatroom: models.Chatroom = context.user.chatroom

    return {
        'url': chatroom.url,
        'messages': [m.to_json() for m in chatroom.messages],
    }


@route('/message', methods=['POST'])
def send_message(context: ApiContext) -> dict:
    """
    req params:
        - text: str
    """
    m = context.user.send_message(context.data['text'])

    return m.to_json()
