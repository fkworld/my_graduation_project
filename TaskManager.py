'''任务管理模块主类
'''

import modelTask


class TaskManager(object):
    def __init__(self):
        print("Load TaskManager module...")
        self.main_task = modelTask.MainTask()

    def init_db(self):
        '''
        初始化数据库
        '''
        modelTask.Base.metadata.create_all(modelTask.Engine)

    def drop_db(self):
        '''
        删除所有数据表
        '''
        modelTask.metadata.drop_all(modelTask.Engine)

    def show_all_task(self):
        '''
        获取所有的task信息
        '''
        all_task = self.main_task.search_all_task()
        return all_task

    def add_task(self, name, info, parameter):
        '''
        添加一个任务
        '''
        self.main_task.add_task(name, info, parameter)
