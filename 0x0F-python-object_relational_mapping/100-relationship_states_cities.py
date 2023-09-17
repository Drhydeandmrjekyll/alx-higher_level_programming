#!/usr/bin/python3
"""Module which adds city and its associated state\
        to MySQL database using SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    # Create SQLAlchemy engine using provided MySQL credentials
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create database tables based on defined models
    Base.metadata.create_all(engine)

    # Create session factory
    Session = sessionmaker(bind=engine)

    # Create session object
    session = Session()

    # Create new city and its associated state
    state = State(name="California")
    city = City(name="San Francisco", state=state)

    # Add new city and associated state to session
    session.add(state)
    session.add(city)

    # Commit session to persist changes in database
    session.commit()
