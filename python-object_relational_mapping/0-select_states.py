#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":

    ''' variables declaration '''
    username: str = sys.argv[1]
    password: str = sys.argv[2]
    db_name: str = sys.argv[3]
    host: str = "localhost"
    port: int = 3306
    statement: str = """SELECT * FROM states ORDER BY id"""

    ''' Connect to MySQL server running locally on port 3306 '''
    db = MySQLdb.connect(
        user=username,
        host=host,
        port=port,
        password=password,
        database=db_name,
    )

    ''' Execute an SQL query to fetch all states '''
    cursor = db.cursor()
    cursor.execute(statement)
    rows = cursor.fetchall()

    ''' Print the results in the desired format '''
    for row in rows:
        print(row)

    ''' Close the cursor and the connection to the database '''
    cursor.close()
    db.close()
    