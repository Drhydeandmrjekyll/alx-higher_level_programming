#!/usr/bin/python3
"""Module which retrieves and prints all cities along with\
        their associated states from MySQL database."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City
from relationship_state import Base, State

if __name__ == "__main__":

    # Get command-line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username, mysql_password, database_name), pool_pre_ping=True)
    # Create all tables if they don't exist
    Base.metadata.create_all(engine)

    # Create configured Session class
    Session = sessionmaker(bind=engine)

    # Create session
    session = Session()

    # Query all City objects and their associated State objects
    cities = session.query(City).join(State).order_by(City.id)

    # Display results
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close session
    session.close()
