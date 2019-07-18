import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine(os.getenv('DATABASE_URL'))
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights = db.execute("Select flight_id, origin, destination, duration from flights").fetchall()
    for flight in flights:
        print(f"{flight.flight_id}. {flight.origin} to {flight.destination} in {flight.duration} minutes.")

    # Prompt usert to choose flight
    flight_Id = int(input("\nFlight_Id: "))
    flight = db.execute("Select origin, destination, duration from flights where flight_id = :id",{"id": flight_Id}).fetchone()

    # Make Sure flight is valid.
    if flight is None:
        return("Error: No such flight.")
    else:
         # List Passengers.
         Passengers = db.execute("Select Pass_name from passenger where flight = :id ",{"id": flight_Id}).fetchall()

         for Passenger in Passengers:
             print("Passenger Name:",Passenger.pass_name)

             if len(Passengers) == 0:
                 print("No passengers.")

if __name__ == "__main__":
    main()
