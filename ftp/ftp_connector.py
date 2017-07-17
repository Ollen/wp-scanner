""" Returns a ftputil connection to the FTP server """
import ftputil

# ftputil test
def ftp_connect():
    # Connect to FTP (try-catch)
    try:
        con = ftputil.FTPHost('localhost', 'admin', 'admin123')
    except ftputil.error.FTPError as e:
        print "[ERROR]: Can't connect to the FTP server"
        print e
        quit()
    else:
        print 'Successfully connected to the FTP server.'
    
    return con

def main():
    ftp_connect()

if __name__ == '__main__':
    main()
