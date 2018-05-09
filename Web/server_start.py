from flask import Flask, Blueprint, render_template
from .view_server import view_server


class ServerStart(object):
    def __init__(self):
        self.app = Flask(__name__)

    def start(self):
        self.init_app()
        self.load_blueprint()
        self.app.run()

    def init_app(self):
        self.app.config['SECRET_KEY'] = '42'
        self.app.config['DEBUG'] = True
        self.load_blueprint()

    def load_blueprint(self):
        self.app.register_blueprint(view_server, url_prefix='')
