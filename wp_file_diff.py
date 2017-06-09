import os, hashlib, datetime

def md5(fname, r_mode='rb'):
    hash_md5 = hashlib.md5()
    with open(fname, r_mode) as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def get_hash_dict(fpath):
    root_count = fpath.count(os.path.sep)
    hash_dict = {}
    for root, dirs, files in os.walk(fpath):
        for x in files:
            if x.endswith('.php'):
                path = os.path.join(root, x)
                path_count = path.count(os.path.sep)
                key_path = path.split('\\')[-(path_count - root_count):]
                hash_dict[os.path.join(*key_path)] = {'hash': md5(path), 'path': path}
    
    return hash_dict

def hash_diff(clean_wp_path, current_wp_path):
    print 'GENERATING hash dictionary'
    orig_hash = get_hash_dict(clean_wp_path)
    curr_hash = get_hash_dict(current_wp_path)
    print '[DONE]: Hash dictionary created'

    print 'COMPARING file hashes...'
    diff_hash = {
        '_scan_time': datetime.datetime.now().strftime("%I:%M %p on %B %d, %Y"),
        '_scanned_wp_path': current_wp_path
        }
    diff = []
    for key in curr_hash:
        if key in orig_hash:
            if curr_hash[key]['hash'] != orig_hash[key]['hash']:
                diff.append({
                    'kind': 'E',
                    'filename': key, 
                    'location': curr_hash[key]['path'],
                    'hash': curr_hash[key]['hash'],
                    'wp_hash': orig_hash[key]['hash'],
                    'wp_location': orig_hash[key]['path']
                })
        else:
            diff.append({
                'kind': 'N',
                'filename': key,
                'location': curr_hash[key]['path'],
                'hash': curr_hash[key]['hash']
            })
    
    diff_hash['diff'] = diff
    print '[DONE]: File hash compared'
    return diff_hash

if __name__ == '__main__':
    clean_path = os.path.dirname(os.path.realpath(__file__)) + '\\wp-files\\4.7.5\\wordpress'
    file_path = 'C:\\xampp\\htdocs\\wordpress'

    different = hash_diff(clean_path, file_path)