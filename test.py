from server import app
from TaskQueue import TaskQueue

# 初始化taskqueue数据表，仅供测试用，生产环境下不应该写这个接口
def init_queue():
    # 以10个任务为测试基准
    for i in range(10):
        _new_task = TaskQueue()
        _new_task.set_download_url("http://localhost:5000/download_sourcefile/REDEME.md")
        _new_task.set_target_node(None)
        _new_task.set_upload_url(None)
        _new_task.add()

def main():
    test = TaskQueue()
    with app.app_context():
        init_queue()

if __name__ == '__main__':
    main()