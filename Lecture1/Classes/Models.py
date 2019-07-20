from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Flight(db.Model):
    __tablename__ = "flights"
    Id = db.Column(db.Integer, primary_key=True)
    Origin = db.Column(db.String, nullable=False)
    Destination = db.Column(db.String, nullable=False)
    Duration = db.Column(db.Integer, nullable=False)
    Passengers = db.relationship("Passengers", backref="flight", lazy=True)
    def Add_Passenger(self,name):
        p = Passengers(name=name, flight_id = self.Id)
        db.session.add(p)
        db.session.commit()

class Passengers(db.Model):
    __tablename__ = "Passengers"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flights.Id"), nullable = False)
