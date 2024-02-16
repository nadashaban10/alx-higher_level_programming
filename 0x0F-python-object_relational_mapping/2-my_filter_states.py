#!/usr/bin/python3
"""a script that lists all states start with N from the database"""

import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursr = db.cursor()
    stateName = sys.argv[4]
    cursr.execute(
   "SELECT * FROM states WHERE name = '{}' \
            ORDER BY id ASC;".format(stateName))
    states = cursr.fetchall()
    for state in states:
        print(state)
