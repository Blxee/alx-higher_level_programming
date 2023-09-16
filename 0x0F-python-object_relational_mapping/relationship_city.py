#!/usr/bin/python3
"""14. Cities in state"""
from relationship_state import Base, State
from sqlalchemy import Column, ForeignKey, Integer, String


class City(Base):
    """Class which represents a City"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
