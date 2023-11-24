#!/usr/bin/python3
"""take arguments and display all values in the states table"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        database=argv[3]
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s \
                ORDER BY id ASC", (argv[4],))

    rows = cur.fetchall()

    for row in rows:
        if row[1] == argv[4]:
            print(row)

    cur.close()
    db.close()
