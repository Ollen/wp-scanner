import os, json
from wp_download import download, extract, compare_zip_hash
from wp_version import identify
from wp_file_diff import hash_diff
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
file_diff = hash_diff(clean_wp_path, file_path)

# Create output directory if it doesn't exist
if not os.path.exists(output_path):
    print 'Creating /output directory.'
    os.makedirs(output_path)

with open(output_path + '\\line-diff.json', 'w') as jsonfile:
    json = json.dumps(file_diff, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '))
    jsonfile.write(json)

# 5. Find Line-diff (Optional)
for key in file_diff:
    if 'kind' in file_diff[key]:
        if file_diff[key]['kind'] == 'E':
            print line_diff(file_diff[key]['wp_location'], file_diff[key]['location'])
        

# 6. Output flagged files