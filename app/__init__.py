# flake8: noqa
# isort:skip_file
from datetime import timedelta

from app.config import Config
from flask import Flask
from flask_sessionstore import Session
from flask_cors import CORS

app: Flask = Flask(__name__)
app.secret_key = Config.SECRET_KEY
app.config.from_object(Config)
Session(app)
CORS(app, supports_credentials=True)


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(hours=24 * 365)


from app.api import *
