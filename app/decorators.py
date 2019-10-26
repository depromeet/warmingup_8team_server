import traceback
from functools import wraps

from app import db
from app.context import ApiContext
from flask import abort, request


def router(application, **kwargs):
    def route(uri, **kwargs):
        def wrapper(fn):
            @wraps(fn)
            def decorator(*args, **kwargs):
                session = db.create_session()
                res = None
                try:
                    context = ApiContext(session=session, request=request)
                    kwargs['context'] = context
                    res = fn(*args, **kwargs)
                    context.session.commit()
                except Exception as e:
                    print(traceback.format_exc())
                    session.rollback()
                    return abort(400, e)
                finally:
                    session.close()
                return res

            application.add_url_rule(uri, fn.__name__, decorator, **kwargs)
            return decorator

        return wrapper

    return route
