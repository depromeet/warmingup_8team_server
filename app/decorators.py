from functools import wraps
from typing import Iterable

from app import hug
from app.context import ApiContext
from app.db import create_session


def route(path, methods: Iterable = frozenset([]), *args, **kwargs):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs) -> dict:
            session = create_session()
            try:
                context = ApiContext(session)
                res = fn(context, *args, **kwargs)
                if type(res) is not dict:
                    raise

                return res
            except Exception as e:
                session.rollback()
                print(e)
                return {'error': e}

        for m in methods:
            method = getattr(hug, m.lower())(path, *args, **kwargs)
            method(wrapper)

        return wrapper

    return decorator
