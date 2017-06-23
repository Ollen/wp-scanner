import mysql.connector
from mysql_connector import mysql_connect

# Insert scan statement
add_scan = ("INSERT INTO diff_scan "
            "(scan_time, wp_version, path_location)"
            "VALUES (%s, %s, %s)")

# Insert diff statement
add_diff = ("INSERT INTO file_diffs "
            "(scan_id, filename, file_hash, wp_hash, location, wp_location, line_diff)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s)")

def insert_scan(data):
    # Get the MySQL connection and cursor
    con, cursor = mysql_connect()
    
    # Insert new scan document
    scan_data = (data['scan_time'], data['wp_version'], data['path_location'])
    try:
        cursor.execute(add_scan, scan_data)
        scan_id = cursor.lastrowid
    except mysql.connector.Error as err:
        print '[ERROR]: Error inserting scan_data in db: {}'.format(err)
        return False
    
    print '[DONE] Successfully inserted a scan with an id of {}'.format(scan_id)
    con.commit()
    cursor.close()
    con.close()

    return True


        