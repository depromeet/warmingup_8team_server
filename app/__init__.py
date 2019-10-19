import json

import hug
from app import api, models
from app.db import create_session
from app.decorators import route


@hug.request_middleware()
def request(request: hug.Request, response: hug.Response):
    request.context["packet"] = models.Packet(
        request_header=request.headers, request_body=request.params
    )


@hug.response_middleware()
def response(request: hug.Request, response: hug.Response, resource):
    session = create_session()
    try:
        packet = request.context['packet']
        packet.response_header = response.headers
        packet.response_body = json.loads(response.data)
        session.add(packet)
        session.commit()
    except Exception:
        session.rollback()


@hug.extend_api()
def apis():
    return [api]


@route("/", methods=["GET"])
def index(context) -> dict:
    return {"id": "123", "text": "test"}
