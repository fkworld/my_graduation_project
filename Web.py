'''Web模块主类
'''
import flask


class Web(object):
    def __init__(self):
        print("Load Web module...")
        self.app = flask.Flask(__name__)

    def start(self):
        self.init_app()
        self.app.run()

    def init_app(self):
        self.app.config['SECRET_KEY'] = '42'
        self.app.config['DEBUG'] = True
        self.load_blueprint()

    def load_blueprint(self):
        from web_flask.view_server import view_server
        self.app.register_blueprint(view_server, url_prefix='')
