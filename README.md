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

### `ftp_connector.py`
Returns a `ftputil` connection instance of the FTP server.

### `mysql_connector.py`
Returns a MySQL connection instanace and cursor.

### `mysql_insert.py`
Inserts the file and line diff result in the MySQL database.

### `wp_deptect.py`
Finds the WordPress directory and its version in the FTP server.

### `wp_download.py`
Downloads the raw WordPress file version and its md5 hash.

### `wp_file_diff.py`
Returns a hash diff dictionary of two WordPress directories.

### `wp_file_hash.py`
Retrieves the WordPress file hashes inside the FTP server and the raw downloaded version.

### `wp_line_diff.py`
Returns the line diff of two files.