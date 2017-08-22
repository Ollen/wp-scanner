""" Returns a MySQL Connection """
import mysql.connector
from ftp_db_config import get_config
from mysql.connector import errorcode

# Modify config to connect to a MySQL database
config = get_config()


def mysql_connect():
    """ Returns the MySQL connection and cursor. """
    # Set connection to None by default.
    con = None
    cursor = None

    try:
        print 'CONNECTING to MySQL DB...'
        con = mysql.connector.connect(**config)
        cursor = con.cursor()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print '[ERROR]: Invalid username and password credentials'
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print '[ERROR]: Databse does not exist'
        else:
            print (err)
        quit()
    
    return con, cursor
    
