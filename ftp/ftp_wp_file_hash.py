""" Diff wordpress files through FTP server """
import hashlib, os, json
from ftp_connector import ftp_connect

def ftp_file_hash():
    """ Get the file hashes inside the FTP server """

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

    # Function to get WordPress hash via FTP
    def get_hash_dict():
        """ Returns the hash dictionary of php files inside the ftp server """
        
        hash_dict = {}
        for root, dirs, files in con.walk('.'):
            for x in files:
                if x.endswith('.php'):
                    path = os.path.normpath(con.path.join(root, x))
                    hash_dict[path] = {'hash': get_md5(path), 'path': path}
        return hash_dict

    # Change to the Wordpress Dir.
    con.chdir('wordpress')

    # Get Hash Dictionary
    print 'GENERATING hash dictionary...'
    ftp_hash_dict = get_hash_dict()

    # Close Directory
    con.close()

    return ftp_hash_dict

def clean_file_hash(dpath):
    """ Get the file hashes of the clean WP version 
    
    Assumes that the given version in the parameter already exists
    in the 'file-wp' directory.
    """

    def md5(fname, r_mode='rb'):
        """ Returns a md5 hash string of a given filename """        
        hash_md5 = hashlib.md5()
        with open(fname, r_mode) as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()

    # Find all .php files and store it in an object
    root_count = dpath.count(os.path.sep)
    hash_dict = {}
    for root, dirs, files in os.walk(dpath):
        for x in files:
            if x.endswith('.php'):
                path = os.path.join(root, x)
                path_count = path.count(os.path.sep)
                key_path = path.split('\\')[-(path_count - root_count):]
                hash_dict[os.path.join(*key_path)] = {'hash': md5(path), 'path': path}
    
    return hash_dict


if __name__ == '__main__':
    ftp_hash = ftp_file_hash()

    """ Testing Puporses """
    output_path = os.path.dirname(os.path.realpath(__file__)) + '\\output'
    with open(output_path + '\\ftp_file_hash.json', 'w') as jsonfile:
        json_output = json.dumps(ftp_hash, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
        jsonfile.write(json_output)


    # dir_path = os.path.dirname(os.path.realpath(__file__))
    # output_path = dir_path + '\\output'
    # wp_files_path = dir_path + '\\wp-files'
    # ver = 4.8
    # clean_wp_path = '{}\\{}\\wordpress'.format(wp_files_path, ver)

    # ftp_diff = clean_file_hash(clean_wp_path)

    # with open(output_path + '\\file-diff-ftp.json', 'w') as jsonfile:
    #     json_output = json.dumps(ftp_diff, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
    #     jsonfile.write(json_output)
