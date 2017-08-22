""" Finds the WordPress dir. and detect its version in the FTP server """
import re
from os.path import normpath, join
#from ftp_connector import ftp_connect


def find_wp_dir(con, wp_path):
    """ Finds the WP file directory in the FTP server 
    Change the connection directory if given WP directory is valid. (wp_path)
    Otherwise, current FTP will be used.
    """
    if wp_path != None:
        print 'SCANNING {} for WP version...'.format(wp_path)
        if con.path.exists(con.path.normpath(wp_path)):
            con.chdir(con.path.normpath(wp_path))
            return
        print '[WARNING]: Given WP path not found.'

    print 'SCANNING current FTP directory...'

def get_wp_ver(con):
    """ Finds the WP version in the FTP server.
    Searches for 'version.php' in the given WP file.
    'max_dept' variables contains the search depth of the WP directory.

    Returns the WP version <string>.
    Closes the FTP connection and exits the program if 'version.php' is not found or
    could not find WP version in 'version.php'
    """
    filename = 'version.php'
    max_depth = 1

    print 'LOCATING "version.php"...'
    file_location = None
    for root, dirs, files in con.walk('.'):
        cur_depth = root.count(con.sep)
        if (filename in files) and (cur_depth <= max_depth):
            file_location = join(normpath(root), normpath(filename))
            print '[DONE]: WP version located at: {}'.format(file_location)

    if (not file_location):
        print '[ERROR]: Could not find "version.php"'
        con.close()
        quit()

    print 'SCANNING wp version...'
    with con.open(file_location, 'r') as f:
        filetext = f.read()
    
    version = re.findall("\\$wp_version = '(.+)';", filetext)
    if not version:
        print '[ERROR]: Could not find WP version in "version.php"'
        con.close()
        quit()
    
    print '[DONE]: Found WP version {}'.format(version[0])
    return version[0]

def detect_wp(con, wp_path):
    """ Finds the WP dir and version 
    Main module for getting WP version.

    Keyword Arguments:
    con     -- <Object> FTPutil conncetion Instance.
    wp_path -- <String> Directory path of the WP in the FTP server.
    """
    find_wp_dir(con, wp_path)
    return get_wp_ver(con)