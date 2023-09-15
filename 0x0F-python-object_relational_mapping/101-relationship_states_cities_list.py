#!/usr/bin/python3
"""16. List relationship"""
from sys import argv
from sqlalchemy import asc, create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':

    engine = create_engine(
        f'mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    cities = Table('cities', MetaData(), autoload_with=engine)
    states = Table('states', MetaData(), autoload_with=engine)
    Session = sessionmaker(bind=engine)
    with Session() as session:
        result = (session
                  .query(states, cities)
                  .join(cities, states.c.id == cities.c.state_id)
                  .order_by(asc(states.c.id), asc(cities.c.id))
                  .all())
        pre_state = -1
        for row in result:
            if row[0] != pre_state:
                print(f'{row[0]}: {row[1]}')
                pre_state = row[0]
            print(f'    {row[2]}: {row[4]}')
