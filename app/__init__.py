import hug


@hug.get('/')
def index():
    return 'hello world'
