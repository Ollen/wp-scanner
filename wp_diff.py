""" Identify diff changes in a WordPress file by comparing it to their original raw version. """
import os, json, datetime
from wp_download import download, extract, compare_zip_hash
from wp_version import identify
from wp_file_diff import file_hash_diff
from wp_line_diff import file_line_diff
from mysql_insert import insert_scan

# Reference for the current dir. path of the script.
dir_path = os.path.dirname(os.path.realpath(__file__))

# Store the downloaded WordPress files for hash and line comparision.
wp_files_path = dir_path + '\\wp-files'

# Stores the output path of the JSON files.
# By default it is the current dir path of this script.
output_path = dir_path + '\\output'

def wp_diff(file_path):
    """ Returns a diff JSON file of both file and line diffs.

    Keyword arguments:
    path -- <String> The dir. path of the WordPress to be scanned. (e.g. 'C:\\xampp\\htdocs\\wordpress')
    """

    # 2. Identify WP version
    ver = identify(file_path)

    # Build scan meta-data
    scan_data = {
        '_scan_time': datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S"),
        '_path_location': file_path,
        '_wp_version': ver
    }

    # 3. Download file and hash if it doesn't exist
    zip_path = '{}\\wordpress-{}.zip'.format(wp_files_path, ver)

    if not os.path.exists(zip_path):
        download(ver)
    elif not compare_zip_hash(ver): # Check if .zip is not tampered
        download(ver)

    extract(ver)

    # 4. Compare Hashes & Export JSON diff
    # All file diffs will be stored here.
    file_diff = {
        '_scan_data': scan_data
    }
    clean_wp_path = '{}\\{}\\wordpress'.format(wp_files_path, ver)
    file_diff.update(file_hash_diff(clean_wp_path, file_path)) 

    # Create output directory if it doesn't exist
    if not os.path.exists(output_path):
        print 'Creating /output directory.'
        os.makedirs(output_path)
    # file_diff JSON output
    with open(output_path + '\\file-diff.json', 'w') as jsonfile:
        json_output = json.dumps(file_diff, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
        jsonfile.write(json_output)

    # 5. Find Line-diff (Optional)
    # All line diffs will be stored here.
    line_diff = {
        '_scan_data': scan_data
    }
    # The line_diff dictionary will only contain edited files.
    for diff in file_diff['diff']:
        if diff['type'] == 'E':
            line_diff[diff['filename']] = file_line_diff(diff['wp_location'], diff['location'])
    # line_diff JSON output
    with open(output_path + '\\line-diff.json', 'w') as jsonfile:
        json_output = json.dumps(line_diff, ensure_ascii=False, sort_keys=True ,indent=4, separators=(',', ': '))
        jsonfile.write(json_output)

    # 6. Insert Data in MySQL DB.
    insert_scan(scan_data, file_diff, line_diff)

# For testing purposes
if __name__ == '__main__':
    wp_diff('C:\\xampp\\htdocs\\wordpress')