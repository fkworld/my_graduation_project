'''任务管理模块主类
'''


import modelTask


class TaskManager(object):
    """[任务管理类]
    """

    def __init__(self):
        """[初始化任务管理类]
        """
        print("Load TaskManager module...")
        self.main_task = modelTask.MainTask()
        self.task_queue = modelTask.TaskQueue()

    def init_db(self):
        '''
        初始化数据库
        '''
        modelTask.Base.metadata.create_all(modelTask.Engine)

    def drop_db(self):
        '''
        删除所有数据表
        '''
        modelTask.Base.metadata.drop_all(modelTask.Engine)

    def show_all_task(self):
        '''
        获取所有的task信息
        '''
        all_task = self.main_task.search_all_task()
        return all_task

    def show_all_queue(self):
        all_task_queue = self.task_queue.search_all_task()
        print(len(all_task_queue))
        return all_task_queue

    def add_task(self, name, info, parameter):
        '''
        添加一个任务
        '''
        self.main_task.add_task(name, info, parameter)

    def add_task_in_queue(self, id):
        """将一个任务添加到任务队列中
        重复100次

        Arguments:
            id {number} -- 任务id
        """
        a_task = self.main_task.search_task_by_id(id)
        for i in range(100):
            self.task_queue.put_main_task_in_queue(a_task)

    def get_task_in_queue(self):
        """[从任务队列中获取任务]
        """
        task = self.task_queue.get_main_task_in_queue()
        print(task)
        return task
