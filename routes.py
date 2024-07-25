from flask import Blueprint, render_template, request, jsonify
from models import RainfallData, HumidityData
import utils

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@main.route('/data')
def data():
    rainfall_data = utils.get_rainfall_data()
    humidity_data = utils.get_humidity_data()
    return jsonify({'rainfall': rainfall_data, 'humidity': humidity_data})