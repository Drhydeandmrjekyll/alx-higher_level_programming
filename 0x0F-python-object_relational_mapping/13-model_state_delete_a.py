#!/usr/bin/python3
"""Module which deletes states containing letter\
        "a" from MySQL database using SQLAlchemy."""
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
    # Retrieve all states from database
    for state in session.query(State):
        # Check if state's name contains letter "a"
        if "a" in state.name:
            # Delete state from session
            session.delete(state)
    # Commit session to persist changes
    session.commit()
