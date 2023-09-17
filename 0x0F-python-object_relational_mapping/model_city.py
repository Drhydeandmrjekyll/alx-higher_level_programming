#!/usr/bin/python3

# Define City model
# Inherits SQLAlchemy Base and links to MySQL table cities.

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represents City for MySQL database.

    Attributes:
        id (str): City's id
        name (sqlalchemy.Integer): City's name.
        state_id (sqlalchemy.String): City's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
