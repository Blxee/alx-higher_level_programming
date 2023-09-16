#!/usr/bin/python3
"""12. Update a state"""
from model_state import Base, State
from sys import argv
from sqlalchemy import asc, create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine(
        f'mysql://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}')
    Session = sessionmaker(bind=engine)
    with Session() as session:
        state = session.query(State).filter_by(id=2).first()
        state.name = 'New Mexico'
        session.commit()
