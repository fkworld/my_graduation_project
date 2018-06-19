
import TaskManager

def main():
    # #s = NodeSourceManager.NodeSourceManager()
    # #s.init_blender_path()
    # #s.run_blender("untitled.blend")

    from server_start import server
    a = server.task_manager.get_task_in_queue()
    print(a.passcode)

if __name__ == '__main__':
    main()
