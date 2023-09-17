#!/usr/bin/python3
"""Module which defines the state class representing state in MySQL database."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents state for MySQL database.

    __tablename__ (str): The name of MySQL table to store states.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.String): The state's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128),nullable=False)
