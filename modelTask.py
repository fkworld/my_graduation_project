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

Base = declarative_base()  # 创建对象的基类
Engine = create_engine('sqlite:///database/Task.db', encoding='utf-8')
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

    def generate_passcode(self, name, update_time):
        '''
        根据传输的name和update_time计算md5值
        '''
        hash = hashlib.md5()
        hash.update(name.encode("utf8"))
        hash.update(update_time.encode("utf8"))
        passcode = hash.hexdigest()
        print("Test: generated passcode = ", passcode)
        return passcode

    def generate_update_time(self):
        '''
        根据当前时间生成updatetime字符串
        '''
        update_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        print("Test: generated update_time = ", update_time)
        return update_time

    def set_sourcefile(self):
        '''
        根据上传文件设定sourcefile的相关信息
        '''
        self.sourcefile_path = "source_file_path"
        self.sourcefile_url = "source_file_url"

    def set_resultfile(self):
        '''
        设定渲染结果文件的相关信息
        '''
        self.resultfile_path = "result_file_path"
        self.resultfile_url = "result_file_url"

    def add_task(self, name, info, parameter):
        '''
        添加一个任务信息到数据库中
        '''
        self.name = name
        self.info = info
        self.parameter = parameter
        self.update_time = self.generate_update_time()
        self.passcode = self.generate_passcode(self.name, self.update_time)
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


class TaskQueue(object):
    """任务队列类
    任务队列最好使用redis写入，这里demo阶段直接保存在内存中
    """

    def __init__(self):
        """[初始化一个无限制的队列]
        """
        self.queue_name = 'test_queue'
        self.queue = queue.Queue(maxsize=0)

    def put_main_task_in_queue(self, main_task):
        """[将任务放入任务队列中]

        Arguments:
            main_task {[type]} -- [description]
        """
        self.queue.put_nowait(main_task)

    def get_main_task_in_queue(self):
        """[从队列中取任务]

        Returns:
            [MainTask()] -- [一个主任务类的实例]
        """
        main_task = self.queue.get_nowait()
        return main_task
