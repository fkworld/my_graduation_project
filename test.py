
import TaskManager

def main():
    # #s = NodeSourceManager.NodeSourceManager()
    # #s.init_blender_path()
    # #s.run_blender("untitled.blend")

    # TM = TaskManager.TaskManager()
    
    # # TM.drop_db()
    # # TM.init_db()
    # TM.get_task_in_queue()
    import json
    data = {
        "id":1
    }
    json_str = json.dumps(data)
    print(json_str)


if __name__ == '__main__':
    main()
