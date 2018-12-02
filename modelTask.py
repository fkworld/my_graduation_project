'''
任务类
可以分成：用户级任务、主任务、子任务
这里作为demo只有一个主任务级
'''

import datetime
import hashlib
import queue

from sqlalchemy import Column, Integer, String, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import WEB_UPLOAD, FTP_HOST, FTP_PORT


Engine = create_engine('sqlite:///database/Task.db', encoding='utf-8', echo=True)
Base = declarative_base()  # 创建对象的基类
Session = sessionmaker(bind=Engine)
session = Session()


class MainTask(Base):
    __tablename__ = 'main_task'

    index = Column(Integer, primary_key=True)  # 序号，自增
    passcode = Column(String(32))  # 使用md5生成唯一验证码
    name = Column(String(64))  # 任务名称
    info = Column(Text)  # 任务说明
    parameter = Column(Text)  # 任务执行参数
    sourcefile_path = Column(String(64))  # 渲染源文件path
    sourcefile_url = Column(String(64))  # 渲染源文件url
    resultfile_path = Column(String(64))  # 渲染结果文件path
    resultfile_url = Column(String(64))  # 渲染结果文件url
    status = Column(Integer, default=0)  # 任务状态码
    update_time = Column(String(64))  # 最后更新时间

    def set_passcode(self):
        """生成passcode"""
        hash = hashlib.md5()
        hash.update(self.name.encode("utf8"))
        hash.update(self.update_time.encode("utf8"))
        self.passcode = hash.hexdigest()

    def set_update_time(self):
        """根据当前时间生成updatetime字符串"""
        self.update_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    def set_sourcefile(self):
        """根据文件信息生成源文件的path和url"""
        self.sourcefile_path = str(self.passcode) + '.' + self.file_ext
        self.sourcefile_url = 'ftp://' + FTP_HOST + ':' + \
            str(FTP_PORT) + '/' + self.sourcefile_path

    def set_resultfile(self):
        '''
        设定渲染结果文件的相关信息
        '''
        self.resultfile_path = "result_file_path"
        self.resultfile_url = "result_file_url"

    def add_task(self, name, info, parameter, file_ext):
        """添加一个任务信息到数据库中"""
        self.name = name
        self.info = info
        self.parameter = parameter
        self.file_ext = file_ext
        self.set_update_time()
        self.set_passcode()
        self.set_sourcefile()
        self.set_resultfile()
        session.add(self)
        session.commit()

    def search_all_task(self):
        """查询所有任务

        Returns:
            list(MainTask()) -- 所有任务列表
        """

        result = session.query(MainTask).all()
        return result

    def search_task_by_id(self, id):
        """根据id查询task

        Arguments:
            id {number} -- 待查询的id

        Returns:
            MainTask() -- 查询结果
        """

        result = session.query(MainTask).filter_by(index=id).one()
        return result

    # 将obj文件转换成js文件
    def process_obj_to_js(self, obj_filepath):
        from subprocess import Popen
        cmd = 'python jObj.py -i ' + obj_filepath + ' -o out/test.js'
        Popen(cmd).wait()


class TaskQueue(Base):
    """任务队列类
    任务队列最好使用redis写入，这里demo阶段使用sqlite3写入
    """

    __tablename__ = 'task_queue'

    id = Column(Integer, primary_key=True)
    main_task_id = Column(Integer)
    run_node_id = Column(Integer, default=0)

    def put_main_task_in_queue(self, main_task):
        """将任务放入队列数据库中

        Arguments:
            main_task {[type]} -- [description]
        """
        self.main_task_id = main_task.index
        session.add(self)
        session.commit()

    def get_main_task_in_queue(self):
        """从队列数据库中取任务

        Returns:
            [MainTask()] -- [一个主任务类的实例]
        """
        x = 0
        # result = session.query(TaskQueue).filter_by(run_node_id=x).all()[0]
        x = 1
        result = session.query(TaskQueue).filter_by(id=x).all()[0]
        print(result.main_task_id)
        result_task = MainTask()
        result_task = result_task.search_task_by_id(result.main_task_id)
        self = session.query(TaskQueue).filter_by(id=result.id).one()
        self.run_node_id = 1
        session.commit()
        return result_task

    def search_all_task(self):
        """查询所有任务

        Returns:
            list(MainTask()) -- 所有任务列表
        """

        result = session.query(TaskQueue).all()
        return result