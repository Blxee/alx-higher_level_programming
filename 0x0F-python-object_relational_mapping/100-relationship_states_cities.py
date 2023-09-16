#!/usr/bin/python3
"""10. Get a state"""
from relationship_city import City
from relationship_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship


if __name__ == '__main__':
    engine = create_engine(
        f'mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    City.state = relationship('State', back_populates='cities')
    with Session() as session:
        state = State(name='California')
        city = City(name='San Francisco', state=state)
        session.add(state)
        session.add(city)
        session.commit()
