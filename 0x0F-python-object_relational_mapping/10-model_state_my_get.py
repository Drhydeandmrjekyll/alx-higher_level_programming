#!/usr/bin/python3
"""Module which searches for state in MySQL database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create SQLAlchemy engine using provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create session factory
    Session = sessionmaker(bind=engine)

    # Create session object
    session = Session()

    # Search for specified state in database
    found = False
    for state in session.query(State):
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            found = True
            break

    # Print message if state is not found
    if found is False:
        print("Not found")
