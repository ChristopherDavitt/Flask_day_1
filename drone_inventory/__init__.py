from re import A
import site
from flask import Flask
from config import Config
from .site.routes import site
from .authentication.routes import auth
from .api.routes import api
from .cool_cars.routes import cars

app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(api)
app.register_blueprint(auth)
app.register_blueprint(cars)

app.config.from_object(Config)