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
        self.load_modules()

    def load_modules(self):
        self.node_check = NodeCheck.NodeCheck()
        self.node_connect = NodeConnect.NodeConnect()
        self.node_manager = NodeManager.NodeManager()
        self.node_source_manager = NodeSourceManager.NodeSourceManager()
        self.task_manager = TaskManager.TaskManager()
        self.task_schedule = TaskSchedule.TaskSchedule()
        self.web = Web.Web()

    def start(self):
        self.web.start()


server = Server()

if __name__ == '__main__':
    server.start()
