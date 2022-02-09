from re import A
import site
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config
from .site.routes import site
from .authentication.routes import auth
from .api.routes import api
from .cool_cars.routes import cars
from .models import db as root_db


app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(site)
app.register_blueprint(api)
app.register_blueprint(auth)
app.register_blueprint(cars)

root_db.init_app(app)
migrate = Migrate(app, root_db)

