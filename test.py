from TaskQueue import TaskQueue

def main():
    test = TaskQueue(download_url="downlaod",target_node=1,upload_url="upload")
    print(test.to_json())

if __name__ == '__main__':
    main()