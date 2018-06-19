'''
以server方式启动系统
'''

from flask_socketio import emit
import json

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

socketio = server.web.get_socketio()

@socketio.on_error()
def default_error(e):
    print('Error')


@socketio.on('message')
def connect(message):
    print('Get message', message)


@socketio.on('test')
def test(messgae):
    print('Get a test message', message)


@socketio.on('GET_TASK')
def get_a_task():
    # 获取一个task
    TM = TaskManager.TaskManager()
    a = TM.get_task_in_queue()
    # 将task中的部分内容转换成json字符串
    data = {
        'id':a.index,
        'passcode':a.passcode,
        'sourcefile_path':a.sourcefile_path,
    }
    json_str = json.dumps(data)
    # 将json字符串返回
    emit('GET_TASK_response',json_str)


if __name__ == '__main__':
    server.start()
