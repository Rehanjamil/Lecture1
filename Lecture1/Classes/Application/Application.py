import os

from flask import Flask, render_template, request
from Models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

@app.route("/")
def index():
    flights = Flight.query.all()
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
    flight = Flight.query.get(flight_id)
    if flight is None:
        return render_template("error.html", message="No Such flight with that id")
    else:
        flight.Add_Passenger(name)
        return render_template("success.html")

@app.route("/flights")
def flights():
    flights = Flight.query.all()
    return render_template("flights.html", flights=flights)

@app.route("/flights/<int:flight_id>")
def flight(flight_id):
    """List details about single flight"""

    # make sure flight exists.
    flight = Flight.query.get(flight_id)

    if flight is None:
        return render_template("error.html",message= "No such Flight with that id found!")
    else:
        passengers = flight.Passengers
        return render_template("flight.html", flight=flight, passengers=passengers)
