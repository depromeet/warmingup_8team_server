# flake8: noqa
# isort:skip_file
from app.config import Config
from flask import Flask
from flask_cors import CORS

app: Flask = Flask(__name__)
app.secret_key = Config.SECRET_KEY
app.config.from_object(Config)
CORS(app, supports_credentials=True)


from app.api import *
