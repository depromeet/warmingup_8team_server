from app.decorators import route


@route('/login', methods=['GET'])
def login(context) -> dict:

    return {'id': 'asd', 'wadasd': '32fw'}
