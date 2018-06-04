'''
以server方式启动系统
'''

from flask_socketio import emit

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
    print(11111)
    print('Get message', message)


'''
fake_server
'''


@socketio.on('game.ready')
def game_ready(json):
    '''服务器接收到cmd'game.ready'，表示客户端游戏已经准备好了
    返回值：cmd'onStart'，通知客户端可以开始游戏
    '''
    print('get a game.ready message, and json=', str(json))
    emit('onStart', json, broadcast=True)


@socketio.on('game.test')
def gametest(message):
    print('Get a test message', message)


if __name__ == '__main__':
    server.start()
