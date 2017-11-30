from server import app
from TaskQueue import TaskQueue

def main():
    test = TaskQueue()
    # test.set_download_url("http://localhost:5000/download_sourcefile/REDEME.md")
    with app.app_context():
        # test.add()
        test = test.get()
        print(test.id)

if __name__ == '__main__':
    main()