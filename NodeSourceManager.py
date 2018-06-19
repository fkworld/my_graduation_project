'''节点依赖资源管理模块主类
'''

import subprocess
from ftplib import FTP

from config import FTP_FILE_PATH, FTP_HOST, FTP_PASSWORD, FTP_PORT, FTP_USER


class NodeSourceManager(object):
    def __init__(self):
        print("Load NodeSourceManager module...")
        self.init_ftp_client()
        self.init_blender_path()

    def init_blender_path(self):
        '''设置blender的渲染器path
        '''
        self.blender_path = 'F:/test/blender.exe'  # blender的path
        self.sourcefile_path = '/upload/'  # 源文件的起始相对path
        # 输出文件path # 其实是构建了一个带path的filename
        self.resultfile_path = '//result/result_####'

    def run_blender(self, sourcefile_path):
        '''执行渲染程序
        - sourcefile_path 渲染源文件路径
        - 参数参考：https://docs.blender.org/manual/zh-hans/dev/advanced/command_line/arguments.html
        '''
        cmd_list = []
        cmd_list.append(self.blender_path)
        cmd_list.append(self.sourcefile_path + sourcefile_path)
        cmd_list.append('-b')  # 后台渲染
        cmd_list.append('-o')
        cmd_list.append(self.resultfile_path)  # 不能在渲染路径(-o)之前设置-f/-a参数
        # cmd_list.append('-a')  # 渲染全部帧
        cmd_list.append('-f 1')  # 只渲染第一帧
        cmd_str = ' '.join(cmd_list)
        subprocess.call(cmd_str)

    def init_ftp_client(self):
        """初始化ftp client"""
        self.ftp = FTP()
        self.ftp.connect(FTP_HOST, FTP_PORT)
        self.ftp.login(FTP_USER, FTP_PASSWORD)

    def ftp_download_file(self, remotepath, localpath, bufsize=1024):
        """从FTP服务器上下载文件"""
        with open(FTP_FILE_PATH + localpath, 'wb') as f:
            self.ftp.retrbinary('RETR ' + remotepath, f.write, bufsize)

    def ftp_upload_file(self, remotepath, localpath, bufsize=1024):
        """上传文件到FTP服务器"""
        # 暂时用不到，直接return
        return 
        with open(FTP_FILE_PATH + localpath, 'rb') as f:
            self.ftp.storbinary('STOR ' + remotepath, f, bufsize)
