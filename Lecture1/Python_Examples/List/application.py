import os
from flask import Flask, render_template, request

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

app = Flask(__name__)

engine = create_engine(os.getenv('DATABASE_URL'))
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    flights = db.execute("Select *from flights").fetchall()
    return render_template("index.html", flights=flights)

@app.route("/book", methods=["POST"])
def book():
    """Book a flight."""

    #Get form information.
    name = request.form.get("Name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid Flight Number!")
    # Make Sure Flight Exists.
    if db.execute("Select * from flights where flight_id = :id", {"id": flight_id}).rowcount == 0:
        return render_template("error.html", message="No Such flight with that id")
    else:
        db.execute("Insert into passenger (Pass_name, flight) values (:name, :flight_id)",{"name": name, "flight_id": flight_id})
        db.commit();
        return render_template("success.html")

@app.route("/flights")
def flights():
    Flights = db.execute("select * from flights").fetchall()
    return render_template("flights.html", flights=Flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """List details about single flight"""

    # make sure flight exists.
    flight = db.execute("select * from flights where flight_id = :id",{"id": flight_id}).fetchone()

    if flight is None:
        return render_template("error.html",message= "No such Flight with that id found!")
    else:
        passengers = db.execute("select Pass_name from passenger where flight = :id", {"id": flight_id}).fetchall()
        return render_template("flight.html", flight=flight, passengers=passengers)
