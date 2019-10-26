from sqlalchemy import create_engine


class BaseConfig:
    DB_HOST = "127.0.0.1"
    DB_PORT = 5432
    DB_USERNAME = "dpm123"
    DB_PASSWORD = "dpm"
    DB_NAME = "kkirook"

    SECRET_KEY = 'jaewonseungil!@#'

    @classmethod
    def engine(cls):
        return create_engine(cls.db_url(), pool_size=50, max_overflow=0)

    @classmethod
    def db_url(cls):
        return f"postgresql+psycopg2://{cls.DB_USERNAME}:{cls.DB_PASSWORD}@{cls.DB_HOST}:{cls.DB_PORT}/{cls.DB_NAME}"  # noqa: E501
