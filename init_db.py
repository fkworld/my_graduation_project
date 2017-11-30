from server import app

with app.app_context():
    from server import server_db
    from Task import MainTask
    from TaskQueue import TaskQueue
    server_db.db.create_all()
    print("初始化数据库成功...")