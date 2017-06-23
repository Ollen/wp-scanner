from mysql_connector import mysql_connect

# Get the MySQL connection and cursor
con, cursor = mysql_connect()

# Insert scan statement
add_scan = ("INSERT INTO diff_scan "
            "(scan_time, wp_version, path_location)"
            "VALUES (%s, %s, %s)")

# Insert diff statement
add_diff = ("INSERT INTO file_diffs "
            "(scan_id, filename, file_hash, wp_hash, location, wp_location, line_diff)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s)")

