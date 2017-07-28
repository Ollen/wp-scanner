""" Finds the WordPress dir. and detect its version in the FTP server """
import re
from os.path import normpath, join
from ftp_connector import ftp_connect


def find_wp_dir(con, wp_path):
    """ Finds the WP file directory in the FTP server """
    if wp_path != None:
        print 'SCANNING {} for wp version...'.format(wp_path)
        if con.path.exists(wp_path):
            con.chdir(wp_path)
            return
        print '[WARNING]: Given WP path not found.'

    print 'SCANNING current FTP directory...'

def get_wp_ver(con):
    """ Finds the WP version in the FTP server """
    filename = 'version.php'
    max_depth = 2

    print 'LOCATING "version.php" in WP dir...'
    file_location = None
    for root, dirs, files in con.walk('.'):
        cur_depth = root.count(con.sep)
        if (filename in files) and (cur_depth <= max_depth):
            file_location = join(normpath(root), normpath(filename))
            print '[DONE]: WP version located at: {}'.format(file_location)

    if (not file_location):
        print '[ERROR]: Cannot identify WP version'
        con.close()
        quit()

    print 'SCANNING wp version...'
    with con.open(file_location, 'r') as f:
        filetext = f.read()
    
    version = re.findall("\\$wp_version = '(.+)';", filetext)
    print '[DONE]: Found WP version {}'.format(version[0])
    return version[0]

def detect_wp(con, wp_path):
    """ Finds the WP dir and version """
    find_wp_dir(con, wp_path)
    return get_wp_ver(con)
    


def test():
    """ Testing Purposes """
    con = ftp_connect('localhost', 'admin', 'admin123')
    # Change to the Wordpress Dir.
    detect_wp(con, '\wordpress\hehe')
    con.close()
    

if __name__ == '__main__':
    test()

    