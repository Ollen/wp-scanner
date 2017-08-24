""" Finds the WordPress dir. and detect its version in the FTP server """
import re
from os import walk
from os.path import normpath, join
#from ftp_connector import ftp_connect



def change_wp_dir(con, wp_path):
    """ Changes the WP file directory in the FTP server 
    Change the FTPutil connection directory if given WP directory is valid. (wp_path)
    Otherwise, current FTP will be used.
    """
    if wp_path != None:
        print 'SCANNING {} for WP version...'.format(wp_path)
        if con.path.exists(con.path.normpath(wp_path)):
            con.chdir(con.path.normpath(wp_path))
            return
        print '[WARNING]: Given WP path not found.'

    print 'SCANNING current FTP directory...'

def find_wp_dir(con, clean_wp_path):
    """ Finds the WP file directory based on the directory list of the WP version.
    Change the FTPutil connection directory if a matching directory list exists.
    Otherwise, gracefully exits the program and closes the FTP connection.

    Keyword Arguments:
    con             -- <Object> FTPutil connection Instance.
    clean_wp_path   -- <String> Path of the raw WP version 
    """

    print 'SEARCHING WP parent directory...'
    # 1. Get the directory list of the raw WP given the version
    raw_dirs = walk(clean_wp_path).next()[1]

    # 2. Walk the given FTP direcoty to verify directory exists
    for root, dirs, files, in con.walk('.'):
        if all(x in dirs for x in raw_dirs):
            print '[DONE] WP parent directory found in {}'.format(root)
            # print root
            con.chdir(root)
            return
    
    print '[ERROR] WP key directories not found.'
    quit()

def get_wp_ver(con, search_depth):
    """ Finds the WP version in the FTP server.
    Searches for 'version.php' in the given WP file.
    'max_dept' variables contains the search depth of the WP directory.

    Returns the WP version <string>.
    Closes the FTP connection and exits the program if 'version.php' is not found or
    could not find WP version in 'version.php'

    Keyword Arguments:
    con             -- <Object> FTPutil conncetion Instance.
    search_depth    -- <Integer> A number indicating the search depth limit of the file search traversal.    
    """
    filename = 'version.php'
    max_depth = search_depth

    print 'LOCATING "version.php"...'
    file_location = None
    for root, dirs, files in con.walk('.'):
        cur_depth = root.count(con.sep)
        if (filename in files) and (cur_depth <= max_depth):
            file_location = join(normpath(root), normpath(filename))
            print '[DONE]: WP version located at: {}'.format(file_location)
            break

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

def detect_wp(con, wp_path, search_depth):
    """ Finds the WP dir and version 
    Main module for getting WP version.

    Keyword Arguments:
    con             -- <Object> FTPutil conncetion Instance.
    wp_path         -- <String> Directory path of the WP in the FTP server.
    search_depth    -- <Integer> A number indicating the search depth limit of the file search traversal.
    """
    change_wp_dir(con, wp_path)
    return get_wp_ver(con, search_depth)