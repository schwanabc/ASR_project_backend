from flask import Flask, jsonify
from gevent import pywsgi, monkey
from geventwebsocket.handler import WebSocketHandler
import os

monkey.patch_all()

from req import route

async_mode = 'gevent'

PORT = int(os.environ.get('PORT', 3000))
SECRET_KEY = os.environ.get('SECRET_KEY', 'asdf')
PEER = os.environ.get('PEER', 'false').lower() == 'true'
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY

route.init(app)

if __name__ == '__main__':
    print(f'Server is running on port {PORT}')
    pywsgi.WSGIServer(('', PORT), app, handler_class=WebSocketHandler).serve_forever()