#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username: str = sys.argv[1]
    password: str = sys.argv[2]
    db_name: str = sys.argv[3]
    host: str = "localhost"
    port: int = 3306
    statement: str = """SELECT * FROM cities ORDER BY id"""
    
    # Connect to MySQL server
    db = MySQLdb.connect(
        user=username,
        host=host,
        port=port,
        password=password,
        database=db_name,
    )
    
    # Create a cursor object
    cursor = db.cursor()
    
    # Execute the SQL statement
    cursor.execute(statement)
    
    # Fetch all the rows
    rows = cursor.fetchall()
    
    # Print the results
    for row in rows:
        print(row)
    
    # Close the cursor and database connection
    cursor.close()
    db.close()
