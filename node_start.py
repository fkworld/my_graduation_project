from socketIO_client import SocketIO, BaseNamespace
from NodeSourceManager import NodeSourceManager
import faker


is_down = True


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
        s = NodeSourceManager()
        s.init_blender_path()
        s.run_blender()
        # 渲染成功后，继续获取任务
        is_down = True


def trans_jsonstr_to_obj(json):
    pass


def main():
    with SocketIO('127.0.0.1', 5000, Test, transports='websocket') as client:
        client.emit('GET_TASK')
        client.wait(5)

# fengyong-fake-data
# websocket模式无法持续获取任务，这里采用一个伪数据


def fake_main():
    for i in range(10):
        print("on GET_TASK response:json=", fake_json(i))

# fengyong-fake-data
# 形成一个伪json数据
def fake_json(i):
    md5 = faker.Faker(locals="zh_CN").md5()
    return {
        'id': i,
        'passcode': md5,
        'sourcefile_path': md5+".blender"
    }


if __name__ == '__main__':
    fake_main()
