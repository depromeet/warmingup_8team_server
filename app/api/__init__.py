import requests
from app import app, models
from app.context import ApiContext
from app.decorators import router
from flask import session

route = router(app)


@route('/login', methods=['POST'])
def login(context: ApiContext) -> dict:
    """
    req params:
     - access_token : 유저 인식하기 위한 토큰j
     - chatroom url : optional (str or None)

    scenario
     - access token을 받아서 KAKAO API에 User Info 요청
      - User Info가 없으면 raise
     - User Info가 있으면 진행
     - User Info가 User모델에 있는지 탐색
     - 없으면 생성 후 User정보 내려줌
     - 있으면 User정보 내려줌
    """

    if context.data.get('access_token') is None:
        # TODO(clogic): 구현해야함.
        # Token받아서 Kakao에 User Infomation 요청 + 유저 get_or_create
        raise

    profile = requests.get(
        'https://kapi.kakao.com/v2/user/me',
        headers={'Authorization': f'Bearer {context.data["access_token"]}'},
    ).json()

    if context.user:
        context.user.update(profile['kakao_account'])
        return context.user.to_json()

    if context.user is None:
        user = models.User(profile['kakao_account'])
        context.session.add(user)
        context.session.commit()
        session['user_id'] = user.id
        context.user = user

    if context.data.get('url'):
        chatroom = (
            context.session.query(models.Chatroom)
            .filter(models.Chatroom.url == context.data['url'])
            .first()
        )
        context.user.chatroom = chatroom
    else:
        chatroom = models.Chatroom()
        context.session.add(chatroom)
        context.session.flush()
        context.user.chatroom = chatroom

    return context.user.to_json()


@route('/chatroom', methods=['GET'])
def get_chatroom(context: ApiContext) -> dict:
    chatroom = context.user.chatroom

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