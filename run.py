from app import app
from app.api import socket_io

if __name__ == '__main__':
    socket_io.run(app, debug=True, host='0.0.0.0')
