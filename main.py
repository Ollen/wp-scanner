import os
from wp_download import download, extract
from wp_version import identify
# 1. Locate the WP dir
file_path = 'C:\\xampp\\htdocs\\wordpress'

# 2. Identify WP version
ver = identify(file_path)

# 3. Download file and hash if it doesn't exist
dir_path = os.path.dirname(os.path.realpath(__file__)) + '\\wp-files'
zip_path = '{}\\wordpress-{}.zip'.format(dir_path, ver)

if not os.path.exists(zip_path):
    download(ver)

extract(ver)

# 4. Compare Hashes
# 5. Flag files