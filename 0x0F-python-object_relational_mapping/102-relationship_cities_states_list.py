#!/usr/bin/python3
"""17. From city"""
from sys import argv
from sqlalchemy import asc, create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine(
        f'mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    cities = Table('cities', MetaData(), autoload_with=engine)
    states = Table('states', MetaData(), autoload_with=engine)
    joined = cities.join(states, cities.c.state_id == states.c.id)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        result = session.query(joined).order_by(asc(cities.c.id)).all()
        for row in result:
            print(f'{row[cities.c.id]}: '
                  + f'{row[cities.c.name]} -> '
                  + f'{row[states.c.name]}')
