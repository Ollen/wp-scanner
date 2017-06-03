""" Detect the WordPress version given the file path """
import os, re

def get_filepath(file_path, level=2):
    # Check the version in this file
    filename = 'version.php'
    max_depth = file_path.count(os.path.sep) + level

    if os.path.isdir(file_path) and os.path.exists(file_path):
        for root, dirs, files in os.walk(file_path):
            cur_depth = root.count(os.path.sep)
            if (filename in files) and (cur_depth <= max_depth):
                return os.path.join(root, filename)
        print '[ERROR] Max dir-depth reach, could not find version.php'
        quit() 
    else:
        print '[ERROR]: Invalid directory'
        quit()

def identify(file_path):
    """ Returns the WP version <String> """
    file_path = get_filepath(file_path)
    
    with open(file_path, 'r') as f:
        filetext = f.read()

    version = re.findall("\\$wp_version = '(.+)';", filetext)
    return version[0]

#identify('C:\\xampp\\htdocs\\wordpress')