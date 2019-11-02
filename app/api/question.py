from app import models
from app.api import route
from app.context import ApiContext


@route('/question/sample', methods=['GET'])
def get_question_samples(context: ApiContext) -> dict:
    samples = [
        {'message': '엄마의 생일은 언제일까요?', 'answer': None},
        {'message': '아빠의 생일은 언제일까요?', 'answer': None},
        {'message': '엄마 아빠의 결혼 기념일은?', 'answer': None},
    ]

    return {'samples': samples}


@route('/question', methods=['POST'])
def create_question(context: ApiContext) -> dict:
    """
    usage:
     - Question을 create시 사용합니다
    req params:
     - message (required) -> str
     - answer (required) -> str
    """

    bot = context.user.chatroom.bot
    question = models.Question(
        message=context.data['message'], answer=context.data['answer'], bot=bot
    )
    context.session.add(question)
    context.session.flush()

    return question.to_json()


@route('/question/<int:id>', methods=['POST'])
def update_question(context: ApiContext, id: int) -> dict:
    """
    usage:
     - Question을 update시 사용
    req params:
     - message (required) -> str
     - answer (required) -> str
    """

    question = (
        context.session.query(models.Question)
        .filter(models.Question.id == context.data['id'])
        .first()
    )

    question.message = context.data['message']
    question.answer = context.data['answer']

    return question.to_json()
