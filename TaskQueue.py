from server import server_db

db = server_db.db


'''
任务队列实际上应该用redis等nosql数据库来做，这里稍微简化一下...
'''
class TaskQueue(db.Model):
    __tablename__ = 'task_queue'
    id = db.Column(db.Integer, primary_key=True)        # 任务id
    download_url = db.Column(db.Text)                   # 任务资源下载地址
    target_node = db.Column(db.Integer,default=0)       # 目标节点
    upload_url = db.Column(db.Text)                     # 结果上传地址

    def set_download_url(self, download_url):
        self.download_url = download_url

    def set_upload_url(self, upload_url):
        self.upload_url = upload_url

    def set_target_node(self, target_node):
        self.target_node = target_node

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # 获取队列中的第一项，然后在列表中删除这一项
    def get(self):
        self = self.query.first()
        self.delete()
        return self

    # 转换成字典供给flaskrequest转换成json
    def to_json_dict(self):
        task_json_dict = {
            "id": self.id,
            "download_url": self.download_url,
            "target_node": self.target_node,
            "upload_url": self.upload_url
        }
        return task_json_dict

    # 清理taskqueue数据表，仅供测试用，生产环境下不应该写这个接口
    def clear_queue(self):
        for _task in self.query.all():
            self = _task
            self.delete()
        print('清理数据库成功...')


