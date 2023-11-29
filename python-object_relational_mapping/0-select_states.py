#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    ''' Connect to MySQL server running locally on port 3306 '''
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], db=sys.argv[3], port=3306)

    ''' Execute an SQL query to fetch all states '''
    cur = db.cursor()
    cur = cursor.execute("SELECT * FROM states ORDER BY id")
    rows = cursor.fetchall()

    ''' Print the results in the desired format '''
    for row in rows:
        print(row)

    ''' Close the cursor and the connection to the database '''
    cursor.close()
    db.close()
