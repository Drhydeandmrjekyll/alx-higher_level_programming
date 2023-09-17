#!/usr/bin/python3

"""Module which lists all states from hbtn_0e_0_usa database."""

import sys
import MySQLdb

if __name__ == "__main__":

    # Get MySQL credentials and search name from command-line arguments
    # and # Connect MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()

    # Execute SQL query to retrieve states with specified name
    c.execute("SELECT * \
                 FROM `states` \
                WHERE BINARY `name` = '{}'".format(sys.argv[4]))

    # Fetch all rows and print states
    [print(state) for state in c.fetchall()]
