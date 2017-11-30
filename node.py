import requests


class Node(object):
    def __init__(self):
        self.level = 1
        self.server_host = "localhost"
        self.server_port = 5000
        self.requests_url = "http://" + \
            self.server_host + ":" + str(self.server_port)
        self.current_task = {}              # 节点当前任务

    def self_test(self):
        # 节点的自我检测功能，检测当前状态是否合格
        pass

    def register_to_server(self):
        # 向服务器注册本节点
        result = requests.get(self.requests_url + "/register")
        print(result.text)

    # 向服务器请求任务，获得一个包含任务信息的json，并将任务信息存入自身数据库中
    def ask_task(self):
        result = requests.get(self.requests_url + "/ask_task")
        print(result.json()['download_url'])

    # 下载任务资源文件
    def download_task(self):
        # 节点向服务器请求下载任务资源
        # 由于文件比较大，所以采用stream=True的文件流下载方式
        result = requests.get(self.current_task['download_url'], stream=True)
        filetype = result.headers['_filetype']
        # 这种下载方法可能有问题，比如在网络不稳定的情况下如何进行断点续传问题，参考使用curl工具来实现对资源文件的下载
        # 构建保存的文件名
        try:
            # 如果不存在download目录，则添加download目录
            import os
            if not os.path.exists('download'):
                os.mkdir('download')
        except expression as identifier:
            pass
        finally:
            filename = "download/" + \
                str(self.current_task['id']) + '_sourcefile' + filetype
        with open(filename, "wb") as _sourcefile:
            for chunk in result.iter_content(chunk_size=1024):
                if chunk:
                    _sourcefile.write(chunk)

    def do_task(self):
        # 执行文件，这里还需要用一个redis做任务状态缓存
        pass


def main():
    mynode = Node()
    mynode.current_task = {
        'id': 1, 'download_url': "http://localhost:5000/download_sourcefile/REDEME.md"}
    mynode.download_task()


if __name__ == '__main__':
    main()
