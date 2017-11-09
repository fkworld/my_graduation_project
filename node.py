import requests

class Node(object):
    def __init__(self):
        self.level = 1
        self.server_host = "localhost"
        self.server_port = 5000
        self.requests_url = "http://" + self.server_host + ":" + str(self.server_port)

    def self_test(self):
        # 节点的自我检测功能，检测当前状态是否合格
        pass

    def register_to_server(self):
        # 向服务器注册本节点
        result = requests.get(self.requests_url + "/register")
        print(result.text)

    def get_task(self):
        # 节点向服务器请求任务资源
        # 由于文件比较大，所以采用stream=True的文件流下载方式
        result = requests.get(self.requests_url + "/needtask", stream=True)
        with open("download.md", "wb") as pdf:
            for chunk in result.iter_content(chunk_size=1024):
                if chunk:
                    pdf.write(chunk)

    def do_task(self):
        # 执行文件，这里还需要用一个redis做任务状态缓存
        pass

def main():
    mynode = Node()
    mynode.register_to_server()
    mynode.get_task()

if __name__ == '__main__':
    main()