'''Web模块主类
'''

from .server_start import ServerStart


class Web(object):
    def __init__(self):
        print("Load Web module...")
        self.server = ServerStart()

    def server_start(self):
        self.server.start()
