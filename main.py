import os
from wp_download import download, extract, compare_zip_hash
from wp_version import identify
from wp_diff import hash_diff

dir_path = os.path.dirname(os.path.realpath(__file__)) + '\\wp-files'
# 1. Locate the WP dir
file_path = 'C:\\xampp\\htdocs\\wordpress'

# 2. Identify WP version
ver = identify(file_path)

# 3. Download file and hash if it doesn't exist
zip_path = '{}\\wordpress-{}.zip'.format(dir_path, ver)

if not os.path.exists(zip_path):
    download(ver)
elif not compare_zip_hash(ver): # Check if .zip is not tampered
    download(ver)

extract(ver)
# 4. Compare Hashes
clean_wp_path = '{}\\{}\\wordpress'.format(dir_path, ver)
file_diff = hash_diff(clean_wp_path, file_path)
print file_diff

# 5. Flag files