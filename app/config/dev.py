import redis
from app.config.base import BaseConfig


class Config(BaseConfig):
    SECRET_KEY = 'dfasdfsdf'

    DB_HOST = 'kkirook.cy4xhqwzngh6.ap-northeast-2.rds.amazonaws.com'
    DB_USERNAME = 'kkirook'
    DB_PASSWORD = 'kkirook1234!'
    DB_NAME = 'kkirook'

    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.from_url('redis://127.0.0.1:6370')
