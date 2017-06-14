import os, json
from wp_download import download, extract, compare_zip_hash
from wp_version import identify
from wp_file_diff import file_hash_diff
from wp_line_diff import line_diff

dir_path = os.path.dirname(os.path.realpath(__file__))
wp_files_path = dir_path + '\\wp-files'
output_path = dir_path + '\\output'

# 1. Locate the WP dir
file_path = 'C:\\xampp\\htdocs\\wordpress'

# 2. Identify WP version
ver = identify(file_path)

# 3. Download file and hash if it doesn't exist
zip_path = '{}\\wordpress-{}.zip'.format(wp_files_path, ver)

if not os.path.exists(zip_path):
    download(ver)
elif not compare_zip_hash(ver): # Check if .zip is not tampered
    download(ver)

extract(ver)

# 4. Compare Hashes & Export JSON diff
clean_wp_path = '{}\\{}\\wordpress'.format(wp_files_path, ver)
file_diff = file_hash_diff(clean_wp_path, file_path)

# Create output directory if it doesn't exist
if not os.path.exists(output_path):
    print 'Creating /output directory.'
    os.makedirs(output_path)

with open(output_path + '\\file-diff.json', 'w') as jsonfile:
    json_output = json.dumps(file_diff, ensure_ascii=False, indent=4, separators=(',', ': '))
    jsonfile.write(json_output)

# 5. Find Line-diff (Optional)
line_diff_dict = {
    '_scan_time': file_diff['_scan_time'],
    '_scanned_wp_path': file_diff['_scanned_wp_path'],
    '_wp_version': ver
    }

for diff in file_diff['diff']:
    if diff['kind'] == 'E':
        line_diff_dict[diff['filename']] = line_diff(diff['wp_location'], diff['location'])

with open(output_path + '\\line-diff.json', 'w') as jsonfile:
    json_output = json.dumps(line_diff_dict, ensure_ascii=False, indent=4, separators=(',', ': '))
    jsonfile.write(json_output)