'''节点通信模块主类
包括封装了一些节点与FTP通信的API
'''
from ftplib import FTP


class NodeConnect(object):
    def __init__(self):
        print("Load NodeConnect module...")

    def init_ftp_client(self):
        self.ftp = FTP()
        self.ftp.connect('127.0.0.1', 2121)
        self.ftp.login('user', '12345')
        self.ftp_file_path = "ftp_download_files/"

    def ftp_download_file(self, remotepath, localpath, bufsize=1024):
        '''从FTP服务器上下载文件
        - remotepath 要下载的文件的路径（包括文件名）
        - localpath 下载之后存储的本地路径（包括文件名）
        - bufsize 传输流大小，默认1024
        '''
        with open(self.ftp_file_path + localpath, 'wb') as f:
            self.ftp.retrbinary('RETR ' + remotepath, f.write, bufsize)

    def ftp_upload_file(self, remotepath, localpath, bufsize=1024):
        '''上传文件到FTP服务器
        - remotepath 上传到FTP存储文件路径（包括文件名）
        - localpath 本地文件路径（包括文件名）
        - bufsize 传输流大小，默认1024
        '''
        with open(self.ftp_file_path + localpath, 'rb') as f:
            self.ftp.storbinary('STOR ' + remotepath, f, bufsize)
