import os, json, datetime
from ftp_connector import ftp_connect
from ftp_wp_detect import detect_wp
from ftp_wp_download import download, extract, compare_zip_hash
from ftp_wp_file_diff import file_hash_diff
from ftp_wp_line_diff import file_line_diff

# Reference for the current dir. path of the script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Store the downloaded WordPress files for hash and line comparison
wp_files_path = dir_path + '\\wp-files'

# Store the output path of the JSON files.
# By default it is the current dir path of this script
output_path = dir_path + '\\ouput'

def ftp_wp_diff(host, user, pwd):
    """ Returns a diff JSON file of both file and line diffs.

    Keyword Arguments:
    host -- <String> Hostname of the FTP server
    user -- <String> FTP Username 
    pwd  -- <String< FTP Password
    """

    # 1. Get Connection
    con = ftp_connect(host, user, pwd)

    # 2. Find WP dir. in the FTP server and returns its version
    ver = detect_wp(con)

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

    extract(ver)

    # 4. Compare Hashes and Export JSON diff
    file_diff = {
        '_scan_data': scan_data
    }
    clean_wp_path = '{}\\{}\\wordpress'.format(wp_files_path, ver)
    file_diff.update(file_hash_diff(con, clean_wp_path))

    # Create output directory if it doesn't exist
    if not os.path.exists(output_path):
        print 'Creating /output directory.'
        os.makedirs(output_path)
    # file_diff JSON output
    with open(output_path + '\\file-diff.json', 'w') as jsonfile:
        json_output = json.dumps(file_diff, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
        jsonfile.write(json_output)

    # 5. Find Line-diffs
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
    con.close()


if __name__ == '__main__':
    ftp_wp_diff('localhost', 'admin', 'admin123')





