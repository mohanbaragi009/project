import pandas as pd
from models import RainfallData, HumidityData

def get_rainfall_data():
    data = RainfallData.query.all()
    return [{'date': d.date.strftime('%Y-%m-%d'), 'rainfall': d.rainfall} for d in data]

def get_humidity_data():
    data = HumidityData.query.all()
    return [{'date': d.date.strftime('%Y-%m-%d'), 'humidity': d.humidity} for d in data]