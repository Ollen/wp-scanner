import wp_download
from wp_version import identify
# 1. Locate the WP dir
file_path = 'C:\\xampp\\htdocs\\wordpress'
# 2. Identify WP version
version = identify(file_path)
print version
# 3. Download file and hash if it doesn't exist

# 4. Compare Hashes
# 5. Flag files