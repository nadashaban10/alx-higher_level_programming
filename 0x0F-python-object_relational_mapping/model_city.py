#!/usr/bin/python3
"""a python file that contains the class definition of a cities"""

from sqlalchemy import ForeignKey, Column, Integer, String
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """State class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
