#!/usr/bin/python3
"""Module which adds new state to MySQL database using SQLAlchemy."""
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

    # Create new State object for Louisiana
    louisiana = State(name="Louisiana")
    # Add new state to session
    session.add(louisiana)
    # Commit session to persist changes
    session.commit()
    # Print ID of newly added state
    print(louisiana.id)
