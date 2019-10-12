from functools import wraps
from typing import Iterable

import hug


def route(path, methods: Iterable = frozenset([]), *args, **kwargs):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            res = fn(*args, **kwargs)
            return res

        for m in methods:
            method = getattr(hug, m.lower())(path, *args, **kwargs)
            method(fn)

        return wrapper

    return decorator
