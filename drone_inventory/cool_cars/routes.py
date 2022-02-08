from flask import Blueprint, render_template


cars = Blueprint('cars', __name__, template_folder='cars')


@cars.route('/coolCars')
def coolCars():
    return render_template('cars.html')