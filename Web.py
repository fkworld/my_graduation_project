'''Web模块主类
'''
from flask import Flask
from flask_socketio import SocketIO


class Web(object):
    def __init__(self):
        print("Load Web module...")
        self.app = Flask(__name__)
        self.socketio = SocketIO(self.app)

    def start(self):
        self.init_app()
        # self.app.run()
        self.socketio.run(self.app, port=5000)

    def init_app(self):
        self.app.config['SECRET_KEY'] = '42'
        self.app.config['DEBUG'] = True
        self.app.config['static_floder'] = 'web_flask/static'
        self.load_blueprint()

    def load_blueprint(self):
        from web_flask.view_server import view_server
        self.app.register_blueprint(view_server, url_prefix='')
