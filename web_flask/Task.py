from server import server_db

db = server_db.db


class MainTask(db.Model):
    __tablename__ = 'main_task_tables'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    mname = db.Column(db.String(64))
    sourcefile_path = db.Column(db.String(64))
    sourcefile_url = db.Column(db.String(64))
    resultfile_path = db.Column(db.String(64))
    resultfile_url = db.Column(db.String(64))
    status = db.Column(db.Integer, default=0)

    # 自动生成name
    def set_name(self):
        self.name = "auto-name"

    # 设置mname为玩家给出的参数
    def set_mname(self):
        self.mname = "given-name"

    # 设置sourcefile的path和url
    def set_sourcefile(self):
        self.sourcefile_path = "spath"
        self.sourcefile_url = "surl"

    def add_to_db(self):
        db.session.add(self)
        db.session.commit()

    def searh_all(self):
        return self.query.all()

    def search_by_id(self, id):
        self = self.query.get(id)

    # 将obj文件转换成js文件
    def process_obj_to_js(self, obj_filepath):
        from subprocess import Popen
        cmd = 'python jObj.py -i ' + obj_filepath + ' -o out/test.js'
        Popen(cmd).wait()