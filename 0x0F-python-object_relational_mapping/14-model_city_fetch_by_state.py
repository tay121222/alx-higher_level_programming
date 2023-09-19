#!/usr/bin/python3
"""
Script to print all City objects from
the hbtn_0e_14_usa database
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, City
from model_state import State

if __name__ == "__main__":
    user, passwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
            f"mysql+mysqldb://{user}:{passwd}@localhost:3306/{db}"
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = (
            session.query(City, State)
            .join(State, City.state_id == State.id)
            .all()
            )

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
