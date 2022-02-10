from dataclasses import fields
from email.policy import default
from enum import unique
from lib2to3.pgen2 import token
import uuid
from datetime import datetime
import secrets

#3rd party imports
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_marshmallow import Marshmallow
from sqlalchemy import ForeignKey


# Adding flask security for passwords
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(50), nullable = True, default = '')
    last_name = db.Column(db.String(50), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String, nullable = True, default = '')
    g_auth_verify = db.Column(db.Boolean, default = False)
    token = db.Column(db.String, default='', unique = True)
    data_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    car = db.relationship('Car', backref="owner", lazy=True)

    def __init__(self, email, first_name='', last_name='', id='', password='', token='', g_auth_verify=False):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.token = self.set_token(24)
        self.email = email
        self.g_auth_verify = g_auth_verify

    # These are methods that go to the database
    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def set_token(self, length):
        return secrets.token_hex(length)

    def __repr__(self):
        return f'User {self.email} has been added to the database.'

class Car(db.Model):
    id = db.Column(db.String, primary_key = True)
    make = db.Column(db.String(50))
    model = db.Column(db.String(200))
    series = db.Column(db.String(100))
    year = db.Column(db.String(5))
    engine = db.Column(db.String(100))
    msrp = db.Column(db.Numeric(precision=10, scale=2), nullable=True)
    description = db.Column(db.String(150), nullable=True)
    seats = db.Column(db.String(20), nullable=True)
    weight = db.Column(db.String(50), nullable=True)
    cost_of_production = db.Column(db.Numeric(precision=10, scale=2), nullable=True)
    user_token = db.Column(db.String(200), db.ForeignKey('user.token'), nullable = False)

    def __init__(self, make, model,series,year,engine,msrp, description, seats, weight, cost_of_production,user_token, id=''):
        self.id = self.set_id()
        self.make = make
        self.model = model
        self.series = series
        self.year = year
        self.engine = engine
        self.msrp = msrp
        self.description = description
        self.weight = weight
        self.cost_of_production = cost_of_production
        self.seats = seats
        self.user_token = user_token

    def set_id(self):
        return secrets.token_urlsafe()

    def __repr__(self):
        return f"The following Car has been created: {self.year} {self.make} {self.model} {self.series}."

class CarSchema(ma.Schema):
    class Meta:
        fields = ['id', 'make', 'model','series','year','engine',  'msrp', 'description','seats','weight', 'cost_of_production']

car_schema = CarSchema()
cars_schema = CarSchema(many=True)