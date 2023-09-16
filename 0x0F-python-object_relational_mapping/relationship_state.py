#!/usr/bin/python3
"""6. First state model"""
from sqlalchemy import Column, Integer, MetaData, String
from sqlalchemy.orm import declarative_base, relationship


metadata = MetaData()
Base = declarative_base(metadata=metadata)


class State(Base):
    """Class which represents a State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))
    cities = relationship('City', back_populates='state')
