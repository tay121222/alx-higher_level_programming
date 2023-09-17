#!/usr/bin/python3
"""script that takes in arguments and displays all
values in the states table of hbtn_0e_0_usa where
name matches the argument. But this time, write
one that is safe from MySQL injections!
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = ("SELECT * FROM states where BINARY name = %s")
    cur.execute(query, (sys.argv[4],))
    states = cur.fetchall()

    for state in states:
        print(state)
    cur.close()
    db.close()
