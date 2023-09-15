#!/usr/bin/python3
"""2. Filter states by user input"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    with MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            charset="utf8") as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
                .format(argv[4]))
            query_rows = cur.fetchall()
            for row in query_rows:
                print(row)
