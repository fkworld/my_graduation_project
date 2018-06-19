'''Web模块主类
'''
import time
from multiprocessing import process

from flask import Flask
from flask_socketio import SocketIO
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import ThreadedFTPServer

from config import WEB_UPLOAD, WEB_UPLOAD_TEMP


class Web(object):
    """Web模块
    """
    def __init__(self):
        print('载入Web模块')
        self.app = Flask(__name__)
        self.socketio = SocketIO(self.app, async_mode='eventlet')
        self.ftp_server = None

    def start(self):
        """Web模块中封装的服务器启动方法"""
        self.run_flask_server()
        # self.run_ftp_server()

    def run_flask_server(self):
        """运行flask服务器（包括flask_socketio）"""
        self.init_app()
        self.socketio.run(self.app, port=5000)

    def run_ftp_server(self):
        """运行ftp服务器"""
        self.init_ftp_server()
        self.ftp_server.serve_forever()

    def init_app(self):
        """初始化flask app"""
        self.app.config['SECRET_KEY'] = '42'
        self.app.config['DEBUG'] = True
        self.app.config['static_floder'] = 'web_flask/static'
        self.load_blueprint()

    def load_blueprint(self):
        """载入全部蓝图"""
        from web_flask.view_server import view_server
        from web_flask.view_admin import view_admin
        self.app.register_blueprint(view_server, url_prefix='')
        self.app.register_blueprint(view_admin, url_prefix='/admin')

    def get_socketio(self):
        """获取到flask中定义的socketio上下文"""
        return self.socketio

    def init_ftp_server(self):
        """初始化ftp服务器"""
        # 新建一个用户组
        authorizer = DummyAuthorizer()
        # 将用户名，密码，指定目录，权限 添加到里面
        authorizer.add_user(
            "user", "12345", WEB_UPLOAD, perm="elradfmwMT")
        # 这个是添加匿名用户,任何人都可以访问，如果去掉的话，需要输入用户名和密码，可以自己尝试
        authorizer.add_anonymous(WEB_UPLOAD)
        handler = FTPHandler
        handler.authorizer = authorizer
        address = ('', 5001)
        self.ftp_server = ThreadedFTPServer(address, handler)
