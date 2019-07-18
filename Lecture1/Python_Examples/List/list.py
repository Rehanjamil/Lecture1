import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine(os.getenv('DATABASE_URL'))
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("Select origin, destination, duration from flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination} in {flight.duration} minutes. ")

if __name__ == "__main__":
    main()
