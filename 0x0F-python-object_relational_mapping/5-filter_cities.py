#!/usr/bin/python3
"""script that takes in the name of a state as an
argument and lists all cities
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = ("SELECT GROUP_CONCAT(name SEPARATOR ', ') FROM cities WHERE state_id = (SELECT id from states WHERE name = %s)")
    cur.execute(query, (sys.argv[4],))
    states = cur.fetchall()

    for state in states:
        print(state[0])
    cur.close
    db.close
