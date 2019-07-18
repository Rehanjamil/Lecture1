import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine(os.getenv('DATABASE_URL'))
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("flights.csv")
    reader = csv.reader(f)

    for ori, dest, dura in reader:
        db.execute("Insert into flights (origin, destination, duration) values (:Origin, :Destination, :Duration)",{"Origin": ori, "Destination": dest, "Duration": dura})
        print(f"Added flight from {ori} to {dest} in {dura} minutes. ")
    db.commit()
if __name__ == "__main__":
    main()
