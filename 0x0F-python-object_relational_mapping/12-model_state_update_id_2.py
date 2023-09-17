#!/usr/bin/python3
"""Module which updates name of state in \
        MySQL database using SQLAlchemy."""
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

    # Retrieve state with ID 2 from database
    state = session.query(State).filter_by(id=2).first()
    # Update name of state to "New Mexico"
    state.name = "New Mexico"
    # Commit session to persist changes
    session.commit()
