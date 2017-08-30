# wp-scanner
_A WordPress file diff python module._

## Package Dependencies
The module requires the following packages to be installed:
- **ftputil**
- **requests**
- **mysql-connector**

Use `pip` to install **ftputil** and **requests**.

### **ftputil**
```
pip install ftputil
```

### **requests**
```
pip install requests
```

### **mysql-connector**
The python MySQL connector can be downloaded [here.](https://dev.mysql.com/downloads/connector/python/)

## Usage
The main module filename of the WordPress diff is `ftp_wp_diff.py`.

Sample usage
``` python
import ftp_wp_diff

ftp_wp_diff('localhost', 'admin', 'admin123', '/wordpress')
```
## MySQL Connection
The MySql database connection can be configured using the `db_config.json` file.

## Module Arguments
```python
ftp_wp_diff('host', 'user', 'pwd', wp_path=None, search_depth=3);
```

- _host_ - Hostname of the FTP server.
- _user_ - FTP username.
- _pwd_ - FTP password.
- _wp_path_ (Optional - Default is None) - WordPress directory location in the FTP server.
- _search_depth_ (Optional - Default is 3) - A number indicating the search depth limit of the WordPress version.

## Sub-modules
The following python files are sub modules that is used in the WordPress file diff.

### `db_config.py`
Returns the database config data located in `db_config.json`. 
Creates a `db_config.json` file with default setting if `db_config.json` is not found.

```python
# returns the decoded data in 'db_config.json'
read_config() 
# Checks if the dictionary keys are valid.
check_config_keys(config)
# Creates a 'db_config.json; file if it doesn't exist.
create_default_config()
# Main database config module fetcher
get_config()
```

### `ftp_connector.py`
Returns a `ftputil` connection instance of the FTP server.
```python
# Connects to a FTP server
ftp_connect(host, user, pwd)
```
- `ftp_connect(host, user, pwd)`
  - `host` - (String) Hostname of the FTP server
  - `user` - (String) FTP Username
  - `pwd`  - (String) FTP Password

### `mysql_connector.py`
Returns a MySQL connection instanace and cursor.
```python
# Returns the MySQL connection and cursor
mysql_connect()
```
### `mysql_insert.py`
Inserts the file and line diff result in the MySQL database.
```python
# Returns the insert sql statement of a file diff based on its diff type.
get_diff_stmt(diff_type)
# Returns the diff values that will be inserted based on its diff type.
get_diff_data(scan_id, diff, line_diff)
# Inserts the diff data in the MySQL DB
insert_scan(scan, file_diff, line_diff)
```
- `get_diff_stmt(diff_type)`
  - `diff_type` - (String) A single character representing the diff type.
- `get_diff_data(scan_id, diff, line_diff)`
  - `scan_id`   - (Integer) Last row ID of the inserted of the file diff (scan_data table)
  - `diff`      - (Dictionary) A single diff instance returned by `wp_file_diff.py` 
  - `line_diff` - (Dictionary) Result of the `wp_line_diff.py` module 
- `insert_scan(scan, file_diff, line_diff)`
  - `scan`      - (Dictionary) Diff scan metadata
  - `file_diff` - (Dictionary) Result of the `wp_file_diff.py` module
  - `line_diff` - (Dictionary) Result of the `wp_line_diff.py` module
### `wp_deptect.py`
Finds the WordPress directory and its version in the FTP server.
```python
# Changes the WP file directory of the Ftputil instance.
change_wp_dir(con, wp_path)
# Finds the WP file direcotry based on the directory list if the WP version.
find_wp_dir(con, clean_wp_path)
# Finds teh WP version in the FTP server
get_wp_ver(con, search_depth)
# Calls `change_wp_dir` and `get_wp_dir`
detect_wp(con, wp_path, search_depth)
```
- `change_wp_dir(con, wp_path)`
  - `con` - (Object) FTPutil connection instance
  - `wp_path` - (String) FTP WordPress Path
- `find_wp_dir(con, clean_wp_path)`
  - `con` - (Object) FTPutil connection instance
  - `clean_wp_path` - (String) Raw WordPress path
- `get_wp_ver(con, search_depth)`
  - `con` - (Object) FTPutil connection instance
  - `search_depth` (Integer) Search depth limit of the file search traversal.
- `detect_wp(con, wp_path, search_depth)`
  - `con` - (Object) FTPutil connection instance
  - `wp_path` - (String) FTP WordPress Path
  - `search_depth` - (Integer) Saerch depth limit of the file search traversal.
### `wp_download.py`
Downloads the raw WordPress file version and its md5 hash.
```python
# Returns true if the zip file is not tampered
compare_zip_hash(ver)
# Extracts the given WP version in the \\wp-files dir.
extract(ver)
# Download the WP version and stores it in 'wp-files; directory
download(ver)
```
- `compare_zip_hash(ver)`
  - `ver` - (String) WordPress version
- `extract(ver)`
  - `ver` - (String) WordPress version
- `download(ver)`
  - `ver` - (String) WordPress version
### `wp_file_diff.py`
Returns a hash diff dictionary of two WordPress directories.
```python
file_hash_diff(con, clean_path)
```
- `file_hash_diff(con, clean_path)`
  - `con` - (Object) FTPutil connection instance
  - `clean_path` - (String) Raw WordPress path
### `wp_file_hash.py`
Retrieves the WordPress file hashes inside the FTP server and the raw downloaded version.
```python
# Returns the md5 hash string of a given file
md5(fname, r_mode='rb')
# Get the file hashes inside the FTP server
ftp_file_hash(con)
# Get the file hashes of the clean WP version
clean_file_hash(dpath)
```
- `md5(fname, r_mode='rb')` 
  - `fname` - (String) Path of the file
  - `r_mode` - (String) Read mode. Default is 'rb'
- `ftp_file_hash(con)`
  - `con` - (Object) FTPutil connnection instance
- `clean_file_hash(dpath)`
  - `dpath` - (String) Raw WordPress path
### `wp_line_diff.py`
Returns the line diff of two files.
```python
# Returns line changes
diff_filter(diff)
# Returns an array of unified diff between two files
file_line_diff(con, fpath1, fpath2)
```
- `diff_filter(diff)`
  - `diff` - (Object) - diff result of two files
- `file_line_diff(con, fpath`, fpath2)`
  - `con` - FTPutil connection instance
  - `fpath1` - File path to be diffed
  - `fpath2` - File path to be diffed