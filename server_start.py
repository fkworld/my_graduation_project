from NodeCheck.node_check import NodeCheck
from NodeConnect.node_connect import NodeConnect
from NodeManager.node_manager import NodeManager
from NodeSourceManager.node_source_manager import NodeSourceManager
from TaskManager.task_manager import TaskManager
from TaskSchedule.task_schedule import TaskSchedule
from Web.web import Web


class Server(object):
    def __init__(self):
        print("Start as Server...")

    def load_modules(self):
        self.node_check = NodeCheck()
        self.node_connect = NodeConnect()
        self.node_manager = NodeManager()
        self.node_source_manager = NodeSourceManager()
        self.task_manager = TaskManager()
        self.task_schedule = TaskSchedule()
        self.web = Web()

    def start(self):
        self.web.server_start()


def main():
    pass


if __name__ == '__main__':
    server = Server()
    server.load_modules()
    server.start()
