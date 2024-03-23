#!/usr/bin/python3
"Documentation"


import MySQLdb
import sys

def main():
    # Unpack command line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
