from ftplib import FTP

import NodeSourceManager


def main():
    ftp = FTP()
    ftp.connect('localhost', 5001)
    ftp.login('user', '12345')
    bufsize = 1024
    fp = open("ftp_download_files/download.md", 'wb')
    ftp.retrbinary('RETR ' + "ftp_storage_files/README.md", fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()


def main2():
    client = NodeSourceManager.NodeSourceManager()
    client.init_ftp_client()
    client.ftp_download_file('111.blend','111.blend')


if __name__ == '__main__':
    main2()
