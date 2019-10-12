from sqlalchemy import create_engine


class Config:
    DB_HOST = "127.0.0.1"
    DB_PORT = 5432
    DB_USERNAME = "dpm123"
    DB_PASSWORD = "dpm"
    DB_NAME = "kkirook"

    @classmethod
    def engine(cls):
        return create_engine(cls.db_url(), pool_size=50, max_overflow=0)

    @classmethod
    def db_url(cls):
        return f"postgresql+psycopg2://{Config.DB_USERNAME}:{Config.DB_PASSWORD}@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DB_NAME}"  # noqa: E501
