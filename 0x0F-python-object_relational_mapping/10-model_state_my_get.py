#!/usr/bin/python3
"""
script that prints the State object with the
name passed as argument from the database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user, passwd, db = sys.argv[1], sys.argv[2]
    db, st_name = sys.argv[3], sys.argv[4]
    engine = create_engine(
            f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}"
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    state_id = session.query(State.id).filter(State.name == st_name).scalar()

    if state_id is not None:
        print("{}".format(state_id))
    else:
        print("Not found")

    session.close()
