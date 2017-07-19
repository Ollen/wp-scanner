from ftp_wp_file_hash import ftp_file_hash, clean_file_hash
from os.path import sep

def file_hash_diff(con, clean_path):
    """ Returns a hash diff dictionary of two wp directories. 
    
    The dictionary contains an array of diff files which include their metadata.
    These metadata include:
    kind = 'E' if the file is edited and 'N' if it's a new file,
    location = Location of the filename,
    wp_location = Location of the clean wp_file
    """

    print 'GENERATING hash dictionary...'
    orig_hash = clean_file_hash(clean_path)
    curr_hash = ftp_file_hash(con)
    print '[DONE]: Hash dictionary created'

    print 'COMPARING file hashes...'
    diff_hash = {
        'diff_e_count': 0, # Total number of edited files.
        'diff_n_count': 0, # Total number of new (unique) files.
        'diff_d_count': 0 # Total number of deleted files.
    }
    diff = [] # Holds all diff data
    # Find Edited and New files
    for key in curr_hash:
        if key in orig_hash:
            if curr_hash[key]['hash'] != orig_hash[key]['hash']:
                diff_hash['diff_e_count'] += 1
                diff.append({
                    'type': 'E',
                    'filename': key.split(sep)[-1], 
                    'location': curr_hash[key]['path'],
                    'file_hash': curr_hash[key]['hash'],
                    'wp_hash': orig_hash[key]['hash'],
                    'wp_location': orig_hash[key]['path']
                })
        else:
            diff_hash['diff_n_count'] += 1
            diff.append({
                'type': 'N',
                'filename': key,
                'location': curr_hash[key]['path'],
                'file_hash': curr_hash[key]['hash']
            })
    
    # Find deleted files
    for key in orig_hash:
        if key not in curr_hash:
            diff_hash['diff_d_count'] += 1
            diff.append({
                'type': 'D',
                'filename': key,
                'wp_location': orig_hash[key]['path']
            })
    
    diff_hash['diff'] = diff
    print '[DONE]: File hash compared'
    return diff_hash