from socketIO_client import SocketIO, BaseNamespace


class Test(BaseNamespace):
    def on_connect(self):
        print('[Connected]')

    def on_reconnect(self):
        print('[Reconnected]')

    def on_disconnect(self):
        print('[Disconnected]')


def main():
    with SocketIO('127.0.0.1', 5000, Test, transports='websocket') as client:
        client.emit('message', 'hello world.')
        client.emit('message', 'hello world-2.')
        client.wait(10)


if __name__ == '__main__':
    main()
