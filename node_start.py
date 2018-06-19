from socketIO_client import SocketIO, BaseNamespace



is_down= True
class Test(BaseNamespace):
    def on_connect(self):
        print('[Connected]')

    def on_reconnect(self):
        print('[Reconnected]')

    def on_disconnect(self):
        print('[Disconnected]')

    def on_GET_TASK_response(self, json):
        print('on GET_TASK response,json=', json)
        is_down = False
        # 将json转换成obj

        # 从ftp服务器上下载渲染源文件

        # 渲染

        # 渲染成功后，继续获取任务
        is_down = True


def trans_jsonstr_to_obj(json):


def main():
    with SocketIO('127.0.0.1', 5000, Test, transports='websocket') as client:
        client.emit('GET_TASK')
        client.wait(5)
 

if __name__ == '__main__':
    main()
