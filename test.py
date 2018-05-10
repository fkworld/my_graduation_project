import TaskManager
import NodeManager


def main():

    for i in range(10):
        t = TaskManager.TaskManager()
        n = NodeManager.NodeManager()
        t.add_task("test", "test", "test")
        n.add_node("test", "test")


if __name__ == '__main__':
    main()
