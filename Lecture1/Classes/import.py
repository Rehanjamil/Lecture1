import os
import csv

from flask import Flask, render_template, request
from Models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    f = open("flights.csv")
    reader = csv.reader(f)

    for ori, dest, dura in reader:
        flight = Flight(Origin = ori, Destination = dest, Duration = dura)
        db.session.add(flight)
        print(f"Added flight from {ori} to {dest} lasting {dura} minutes. ")
    db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()
