#!/usr/bin/python3
"""script that takes in the name of a state as an
argument and lists all cities
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = (
            """
            SELECT name FROM cities WHERE
            state_id = (SELECT id from states WHERE name = %s)
            """
            )
    cur.execute(query, (sys.argv[4],))
    states = cur.fetchall()

    results = []
    for state in states:
        results.append(state[0])
    print(", ".join(results))
    cur.close
    db.close
