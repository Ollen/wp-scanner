import ftputil, hashlib
from ftplib import FTP

# Login function
def ftp_login(host, user, password):
    ftp = FTP(host)
    ftp.login(user, password)
    return ftp

# ftputil test
def ftputil_test():
    # Connect to FTP (try-catch)
    try:
        con = ftputil.FTPHost('localhost', 'admin', 'admin123')
    except ftputil.error.FTPError as e:
        print e
        return
    else:
        print 'Successfully connected to the FTP server.'
    
    # Change Directory to Wordpress
    con.chdir('wordpress')
    print con.listdir('.')

    # Read MD5 Hash of a file
    md5 = hashlib.md5()
    with con.open('xmlrpc.php', 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5.update(chunk)
            print md5.hexdigest()

    


    # Close Directory
    con.close()

def main():
    ftputil_test()

if __name__ == '__main__':
    main()
