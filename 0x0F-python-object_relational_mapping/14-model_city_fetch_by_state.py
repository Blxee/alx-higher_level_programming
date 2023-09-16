#!/usr/bin/python3
"""14. Cities in state"""
from model_state import Base, State
from model_city import City
from sys import argv
from sqlalchemy import asc, create_engine, MetaData, Table
from sqlalchemy.orm import relationship, sessionmaker

if __name__ == '__main__':
    engine = create_engine(
        f'mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    Session = sessionmaker(bind=engine)
    with Session() as session:
        result = (session
                  .query(State.name, City.id, City.name)
                  .join(City)
                  .order_by(asc(City.id))
                  .all())
        for state_name, city_id, city_name in result:
            print(f'{state_name}: ({city_id}) {city_name}')
