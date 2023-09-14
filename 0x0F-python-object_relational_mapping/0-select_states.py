#!/usr/bin/python
"""0. Get all states"""
import MySQLdb
from sys import argv

with MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8") as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
