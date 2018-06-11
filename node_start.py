from socketIO_client import SocketIO, BaseNamespace


class Test(BaseNamespace):
    def on_connect(self):
        print('[Connected]')

    def on_reconnect(self):
        print('[Reconnected]')

    def on_disconnect(self):
        print('[Disconnected]')

    def on_GET_TASK_response(self,json):
        print('on GET_TASK response,json=',json)


def main():
    with SocketIO('127.0.0.1', 5000, Test, transports='websocket') as client:
        client.emit('GET_TASK')
        client.wait(5)


if __name__ == '__main__':
    main()
