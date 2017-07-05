from ftplib import FTP

def ftp_login(host, user, password):
    ftp = FTP(host)
    ftp.login(user, password)
    return ftp

def main():
    ftp = ftp_login('localhost', 'admin', 'admin123')
    ftp.cwd('wordpress')
    ftp.retrlines('LIST')

if __name__ == '__main__':
    main()