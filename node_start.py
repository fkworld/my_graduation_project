
from socketIO_client import SocketIO, LoggingNamespace

with SocketIO('127.0.0.1', 5000) as client:
    client.emit('message', 'hello world.')
    # client.emit('error', 'data')
