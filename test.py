import server_start
import flask


def main():
    server_start.server.node_manager.init_db()
    server_start.server.task_manager.init_db()

    server_start.server.node_manager.add_node("1","1")
    server_start.server.task_manager.add_task("1","1","1")


if __name__ == '__main__':
    main()
