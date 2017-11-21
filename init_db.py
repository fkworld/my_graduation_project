from server import app, server_db
from Task import MainTask

with app.app_context():
    server_db.db.create_all()
    print(MainTask.query.all())