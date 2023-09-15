#!/usr/bin/python3
"""4. Cities by states"""
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
                "SELECT cities.id, cities.name, states.name " +
                "FROM cities INNER JOIN states " +
                "ON cities.state_id = states.id " +
                "ORDER BY cities.id ASC")
            query_rows = cur.fetchall()
            for row in query_rows:
                print(row)
