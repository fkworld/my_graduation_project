from flask_sqlalchemy import SQLAlchemy

class ServerDB(object):
    # 传入app，在app中实例化数据库模块
    def __init__(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///server.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        self.db = SQLAlchemy()
        self.db.init_app(app)
    