from server import server_db

class MainTask(server_db.db.Model):
    db = server_db.db
    __tablename__ = 'main_task_tables'
    id = db.Column(db.Integer, primary_key=True)
