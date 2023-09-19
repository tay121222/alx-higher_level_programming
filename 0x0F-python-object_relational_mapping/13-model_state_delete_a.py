#!/usr/bin/python3
"""
Script to delete State objects with a name
containing the letter "a" from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user, passwd = sys.argv[1], sys.argv[2]
    db = sys.argv[3]
    engine = create_engine(
            f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}"
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    delete_state = session.query(State).filter(State.name.like('%a%')).all()

    for state in delete_state:
        session.delete(state)

    session.commit()
    session.close()
