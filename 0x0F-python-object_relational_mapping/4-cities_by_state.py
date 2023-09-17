#!/usr/bin/python3
"""Module which lists all states from hbtn_0e_0_usa database."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get MySQL credentials and search name from command-line arguments
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # Connect MySQL server
    c = db.cursor()

    # Execute SQL query to retrieve all states
    c.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                 FROM `cities` as `c` \
                INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")

    # Fetch all rows and print states
    [print(city) for city in c.fetchall()]
