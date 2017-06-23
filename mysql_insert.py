import mysql.connector
from mysql_connector import mysql_connect

# Insert scan statement
add_scan = ("INSERT INTO diff_scan "
            "(scan_time, wp_version, path_location)"
            "VALUES (%s, %s, %s)")


def get_diff_stmt(diff_type):
    if diff_type == 'E':
        add_diff = ("INSERT INTO file_diffs "
            "(scan_id, type ,filename, file_hash, wp_hash, location, wp_location)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    elif diff_type == 'N':
        add_diff = ("INSERT INTO file_diffs "
            "(scan_id, type ,filename, file_hash, location)"
            "VALUES (%s, %s, %s, %s, %s)")
    elif diff_type == 'D':
        add_diff = ("INSERT INTO file_diffs "
            "(scan_id, type ,filename, wp_location)"
            "VALUES (%s, %s, %s, %s)")
    return add_diff
    

def get_diff_data(scan_id ,diff):
    if diff['type'] == 'E':
        diff_data = (
            scan_id,
            diff['type'], diff['filename'].split('\\')[-1], diff['file_hash'],
            diff['wp_hash'], diff['location'], diff['wp_location']
        )
    elif diff['type'] == 'N':
        diff_data = (
            scan_id,
            diff['type'], diff['filename'].split('\\')[-1], diff['file_hash'], diff['location']
        )
    elif diff['type'] == 'D':
        diff_data = (
            scan_id,
            diff['type'], diff['filename'].split('\\')[-1], diff['wp_location']
        )

    return diff_data

def insert_scan(data):
    # Get the MySQL connection and cursor
    con, cursor = mysql_connect()
    
    # Insert new scan document
    print 'INSERTING data in MySQL...'
    scan_data = (data['scan_time'], data['wp_version'], data['path_location'])
    try:
        cursor.execute(add_scan, scan_data)
        scan_id = cursor.lastrowid
        con.commit()    
    except mysql.connector.Error as err:
        print '[ERROR]: Error inserting scan_data in db: {}'.format(err)
        return False
    
    # Insert diff documents
    for diff in data['diff']:
        try:
            add_diff = get_diff_stmt(diff['type'])
            diff_data = get_diff_data(scan_id, diff)
            cursor.execute(add_diff, diff_data)
            con.commit()
        except mysql.connector.Error as err:
            print '[ERROR]: Error inserting diff_data in db: {}'.format(err)
            return False
        

    print '[DONE] Successfully inserted a scan with an id of {}'.format(scan_id)
    cursor.close()
    con.close()

    return True


        