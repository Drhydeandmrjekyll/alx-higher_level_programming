#!/usr/bin/python3
"""Module which lists all State objects, and corresponding
        City objects, contained in mySQL database"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # Create database engine using provided arguments
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create session factory bound to engine
    Session = sessionmaker(bind=engine)

    # Create session object
    session = Session()

    # Retrieve all states from database and order them by ID
    for state in session.query(State).order_by(State.id):
        # Print state ID and name
        print("{}: {}".format(state.id, state.name))

        # Iterate over cities associated with current state
        for city in state.cities:
            # Print city ID and name
            print("    {}: {}".format(city.id, city.name))
