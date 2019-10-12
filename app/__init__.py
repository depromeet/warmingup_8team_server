import hug
from app import models
from app.decorators import route


@hug.request_middleware()
def request(request: hug.Request, response: hug.Response):
    request.context["packet"] = models.Packet(
        request_header=request.headers, request_body=request.params
    )


@hug.response_middleware()
def response(request: hug.Request, response: hug.Response, resource):
    """packet = request.context['packet']
    packet.response_header = response.headers
    packet.response_body = json.loads(response.data)
    session.add(packet)
    session.commit()"""


@route("/", methods=["GET"])
def index() -> dict:
    return {"id": "123", "text": "test"}
