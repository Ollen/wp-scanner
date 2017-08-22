""" Returns a ftputil connection of the FTP server """
import ftputil

# ftputil test
def ftp_connect(host, user, pwd):
    """ Connects to a FTP server.
    Returns a FTPutil connection instance.

    Keyword Arguments:
    host    -- <String> Hostname of the FTP server
    user    -- <String> FTP Username
    pwd     -- <String> FTP Password
    """
    # Connect to FTP (try-catch)
    try:
        con = ftputil.FTPHost(host, user, pwd)
    except ftputil.error.FTPError as e:
        print "[ERROR]: Can't connect to the FTP server"
        print e
        quit()
    else:
        print 'Successfully connected to the FTP server.'

    return con