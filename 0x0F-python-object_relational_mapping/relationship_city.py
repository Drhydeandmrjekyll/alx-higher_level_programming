#!/usr/bin/python3
"""Module which defines City model representing\
        a city for MySQL database using SQLAlchemy."""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create base class for declarative models
Base = declarative_base()


class City(Base):
    """Represents city for MySQL database.

    Attributes:
        id (sqlalchemy.Column): City's id.
        name (sqlalchemy.Column):City's name.
        state_id (sqlalchemy.Column): City's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
