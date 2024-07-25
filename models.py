from app import db

class RainfallData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    rainfall = db.Column(db.Float, nullable=False)

class HumidityData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    humidity = db.Column(db.Float, nullable=False)