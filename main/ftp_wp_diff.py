import os, json, datetime
from ftp_connector import ftp_connect
from wp_detect import detect_wp, find_wp_dir
from wp_download import download, extract, compare_zip_hash
from wp_file_diff import file_hash_diff
from wp_line_diff import file_line_diff
from mysql_insert import insert_scan
from ftp_img_ver import verify_img_type

# Reference for the current dir. path of the script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Store the downloaded WordPress files for hash and line comparison
wp_files_path = dir_path + '\\wp-files'

# Store the output path of the JSON files.
# By default it is the current dir path of this script
output_path = dir_path + '\\output'

def ftp_wp_diff(host, user, pwd, wp_path=None, search_depth=3):
    """ Returns a diff JSON file of both file and line diffs.
    Also logs the diff in a MySQL database. (See 'db_config.json' for database meta-data)

    Keyword Arguments:
    host            -- <String> Hostname of the FTP server
    user            -- <String> FTP Username
    pwd             -- <String< FTP Password
    wp_path         -- <String> WordPress directory location in the FTP server. [Default is None].
    search_depth    -- <Integer> A number indicating the search depth limit of the WordPress version. [Default is 3]. 
    """

    # 1. Get FTPutil connection instance.
    con = ftp_connect(host, user, pwd)

    # 2. Traverse the given FTP directory and find 'version.php' to get WP version.
    ver = detect_wp(con, wp_path, search_depth)

    #> Build scan meta-data
    scan_data = {
        '_scan_time': datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S"),
        '_ftp_hostname': host,
        '_wp_version': ver
    }

    # 3. Download and extract raw WP version if it doesn't exist
    zip_path = '{}\\wordpress-{}.zip'.format(wp_files_path, ver)
    if not os.path.exists(zip_path):
        download(ver)
    elif not compare_zip_hash(ver): # Check if .zip is not tampered
        download(ver)

    
    clean_wp_path = '{}\\{}\\wordpress'.format(wp_files_path, ver)
    if not os.path.exists(clean_wp_path):
        extract(ver)
        

    # 4. Find the WP parent directory based on the version.
    find_wp_dir(con, clean_wp_path)

    # 5. Compare Hashes and Export JSON diff
    file_diff = {
        '_scan_data': scan_data
    }
    file_diff.update(file_hash_diff(con, clean_wp_path))
    # Create output directory if it doesn't exist
    if not os.path.exists(output_path):
        print 'Creating /output directory.'
        os.makedirs(output_path)
    # file_diff JSON output
    with open(output_path + '\\file-diff.json', 'w') as jsonfile:
        json_output = json.dumps(file_diff, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
        jsonfile.write(json_output)

    # 6. Find Line-diffs
    line_diff = {
        '_scan_data': scan_data
    }
    # The line_diff dictionary will only contain edited files.
    for diff in file_diff['diff']:
        if diff['type'] == 'E':
            line_diff[diff['filename']] = file_line_diff(con, diff['wp_location'], diff['location'])
    # line_diff JSON output
    with open(output_path + '\\line-diff.json', 'w') as jsonfile:
        json_output = json.dumps(line_diff, ensure_ascii=False, sort_keys=True ,indent=4, separators=(',', ': '))
        jsonfile.write(json_output)

    # 7. Insert Data in MySQL DB.
    insert_scan(scan_data, file_diff, line_diff)

    # Optional
    img_list = verify_img_type(con)
    with open(output_path + '\\image.json', 'w') as jsonfile: 
        json_output = json.dumps(img_list, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': ')) 
        jsonfile.write(json_output)

    con.close()
    quit()

if __name__ == '__main__':
    ftp_wp_diff('localhost', 'admin', 'admin123', '/wordpress', 3)