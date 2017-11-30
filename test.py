from server import app
from TaskQueue import TaskQueue

def main():
    test = TaskQueue(download_url="downlaod",target_node=1,upload_url="upload")
    with app.app_context():
        test.add()
        print(test.get())

if __name__ == '__main__':
    main()