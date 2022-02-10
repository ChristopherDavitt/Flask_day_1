from flask import Blueprint, jsonify, request
from flask_login import login_required
from drone_inventory.helpers import token_required
from drone_inventory.models import db, User, Car, car_schema, cars_schema

api = Blueprint('api', __name__, url_prefix = '/api')

@api.route('getdata')
def getdata(current_user_token):
    return jsonify({'some': 'value', 
                    'Other':44.3})

@api.route('/cars', methods=['POST'])
@token_required
def create_car(current_user_token):
    make = request.json['make']
    model = request.json['model']
    series = request.json['series']
    year = request.json['year']
    engine = request.json['engine']
    msrp = request.json['msrp']
    weight = request.json['weight']
    cost_of_production = request.json['cost_of_production']
    seats = request.json['seats']
    description = request.json['description']
    user_token = current_user_token.token 

    car = Car(make, model,series,year, engine, msrp,
            weight, cost_of_production, description, seats, user_token)
    db.session.add(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)

# retrieve ALL car
@api.route('/cars', methods=['GET'])
@token_required
def get_cars(current_user_token):
    owner = current_user_token.token
    cars = Car.query.filter_by(user_token = owner).all()
    response = cars_schema.dump(cars)
    return jsonify(response)


# retrieve a single car
@api.route('/car/<id>', methods=['GET'])
@token_required
def get_car(current_user_token, id):
    owner = current_user_token.token
    car = Car.query.get(id)
    response = car_schema.dump(car)
    return jsonify(response)

@api.route('/cars/<id>', methods=['POST','PUT'])
@token_required
def update_car(current_user_token, id):
    car = Car.query.get(id)

    car.make = request.json['make']
    car.model = request.json['model']
    car.series = request.json['series']
    car.year = request.json['year']
    car.engine = request.json['engine']
    car.msrp = request.json['msrp']
    car.weight = request.json['weight']
    car.cost_of_production = request.json['cost_of_production']
    car.seats = request.json['seats']
    car.description = request.json['description']
    car.user_token = current_user_token.token 

    db.session.commit()
    response = car_schema.dump(car)
    return jsonify(response)

@api.route('/cars/<id>', methods=['DELETE'])
@token_required
def delete_car(current_user_token, id):
    car = Car.query.get(id)
    db.session.delete(car)
    db.session.commit()

    response = car_schema.dump(car)
    return jsonify(response)