#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a  from the database
"""

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    states = session.query(State)
    for state in states:
     if "a" in state.name:
        session.delete(state)
    session.commit()
    session.close()
