import hug
import json

from app.models import *
from app.db import session


@hug.request_middleware()
def request(request: hug.Request, response: hug.Response):
    request.context['packet'] = Packet(request_header=request.headers, request_body=request.params)

@hug.response_middleware()
def response(request, response: hug.Request, resource: hug.Response):
    packet = request.context['packet']
    packet.response_header = response.headers
    packet.response_body = json.loads(response.data)
    session.add(packet)
    session.commit()


@hug.get('/')
def index() -> dict:
    return { 'id': '123', 'text': 'test' }
