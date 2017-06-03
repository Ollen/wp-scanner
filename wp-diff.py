import os, hashlib

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def get_hash_dict(fpath):
    hash_dict = {}
    for root, dirs, files in os.walk(fpath):
        for x in files:
            if x.endswith('.php'):
                path = os.path.join(root, x)
                hash_dict[x] = md5(path)
    
    return hash_dict

def hash_diff(clean_wp_path, current_wp_path):
    orig_hash = get_hash_dict(clean_wp_path)
    curr_hash = get_hash_dict(current_wp_path)
    #Diff the two hash here

#wp_files_path = os.path.dirname(os.path.realpath(__file__)) + '\\wp-files\\4.7.5\\wordpress'

