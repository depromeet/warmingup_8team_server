import hug

from app.models import *


@hug.get('/')
def index():
    return 'hello world'
