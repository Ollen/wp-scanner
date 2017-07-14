""" Diff wordpress files through FTP server """
import hashlib
from ftp_connector import ftp_connect

def ftp_file_diff():
    # Connect and get FTP connection
    con = ftp_connect()

    # Function to get MD5 Hash inside the FTP server
    def get_md5(fpath):
        """ Returns the md5 hash string of a file """
        md5 = hashlib.md5()
        with con.open(fpath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                md5.update(chunk)
        return md5.hexdigest()

    def get_hash_dict():
        """ Returns the hash dictionary of php files inside the ftp server """
        
        hash_dict = {}
        for root, dirs, files in con.walk('.'):
            for x in files:
                if x.endswith('.php'):
                    path = con.path.join(root, x)
                    hash_dict[path] = {'hash': get_md5(path), 'path': path}
        return hash_dict

    # Identify Wordpress Directory
    con.chdir('wordpress')
    print con.listdir('.')
    
    # Close Directory
    con.close()
    return

# Testing/Debugging purposes
if __name__ == '__main__':
    ftp_file_diff()