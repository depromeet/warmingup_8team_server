# flake8: noqa
# isort:skip_file
from typing import Any
from app import app
from app.decorators import router

route: Any = router(app)

from app.api.user import *
from app.api.chat import *
from app.api.question import *
