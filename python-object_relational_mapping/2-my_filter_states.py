#!/usr/bin/python3
"""Documentation"""


import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM states\
                   WHERE states.name = '{sys.argv[4]}'\
                   ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
