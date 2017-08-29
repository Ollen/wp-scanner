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

## Module Arguments
```python
ftp_wp_diff('host', 'user', 'pwd', wp_path=None, search_depth=3);
```

- _host_ - Hostname of the FTP server.
- _user_ - FTP username.
- _pwd_ - FTP password.
- _wp_path_ - WordPress directory location in the FTP server. [Default is None]
- _search_depth_ - A number indicating the search depth limit of the WordPress version. [Default is 3]