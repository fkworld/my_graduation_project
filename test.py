
import TaskManager

def main():
    #s = NodeSourceManager.NodeSourceManager()
    #s.init_blender_path()
    #s.run_blender("untitled.blend")

    TM = TaskManager.TaskManager()
    
    TM.add_task_in_queue(1)


if __name__ == '__main__':
    main()
