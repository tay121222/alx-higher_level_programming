#!/usr/bin/python3
"""
script that changes the name of a State
object from the database
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

    update_state = session.query(State).filter_by(id=2).first()

    if update_state:
        update_state.name = "New Mexico"

    session.commit()
    session.close()
