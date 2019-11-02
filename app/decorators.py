import traceback
import json
from functools import wraps

from app import db, models
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
                    context = create_context(session)
                    kwargs['context'] = context
                    res = fn(*args, **kwargs)

                    '''packet = models.Packet(
                        request_header=dict(context.request.headers),
                        request_body=json.loads(context.request.data.decode()),
                        response_header={},
                        response_body=res,
                    )

                    context.session.add(packet)'''
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


def create_context(session=None):
    if session is None:
        session = db.create_session()
    return ApiContext(session=session, request=request)
