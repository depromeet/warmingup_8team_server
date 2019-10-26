# flake8: noqa
# isort:skip_file
from app.config import Config
from flask import Flask

app: Flask = Flask(__name__)
app.secret_key = Config.SECRET_KEY
app.config.from_object(Config)


from app.api import *
