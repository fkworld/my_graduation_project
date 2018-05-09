'''
以server方式启动系统
'''

import NodeCheck
import NodeConnect
import NodeManager
import NodeSourceManager
import TaskManager
import TaskSchedule
import Web


class Server(object):
    def __init__(self):
        print("Start as Server...")

    def load_modules(self):
        '''
        载入7个模块
        '''
        self.node_check = NodeCheck.NodeCheck()
        self.node_connect = NodeConnect.NodeConnect()
        self.node_manager = NodeManager.NodeManager()
        self.node_source_manager = NodeSourceManager.NodeSourceManager()
        self.task_manager = TaskManager.TaskManager()
        self.task_schedule = TaskSchedule.TaskSchedule()
        self.web = Web.Web()

    def start(self):
        '''
        作为服务器启动
        '''
        self.web.start()


server = Server()
server.load_modules()

if __name__ == '__main__':
    server.start()
