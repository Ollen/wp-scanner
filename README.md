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
### `wp_deptect.py`
Finds the WordPress directory and its version in the FTP server.
```python
# Changes the WP file directory of the Ftputil instance.
change_wp_dir(con, wp_path)
# Finds the WP file direcotry based on the directory list if the WP version.
find_wp_dir(con, clean_wp_path)
# Finds teh WP version in the FTP server
get_wp_ver(con, search_depth)
# detect_wp(con, wp_path, search_depth)
```
### `wp_download.py`
Downloads the raw WordPress file version and its md5 hash.
```python


```
### `wp_file_diff.py`
Returns a hash diff dictionary of two WordPress directories.
```python

```
### `wp_file_hash.py`
Retrieves the WordPress file hashes inside the FTP server and the raw downloaded version.
```python

```
### `wp_line_diff.py`
Returns the line diff of two files.
```python

```