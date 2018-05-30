from ftplib import FTP


def main():
    ftp = FTP()
    ftp.connect('127.0.0.1', 2121)
    ftp.login()
    bufsize = 1024
    fp = open("ftp_download_files/download.md", 'wb')
    ftp.retrbinary('RETR ' + "ftp_storage_files/README.md", fp.write, bufsize)
    ftp.set_debuglevel(0)
    fp.close()


if __name__ == '__main__':
    main()
