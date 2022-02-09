import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

# gives access to the project in any OS we find mac, pc, etc.
# allows outside files/folders to be added to the project from the base directory

load_dotenv(os.path.join(basedir,'.env'))

class Config:
    # FLASK_ENV
    """
    Set Config variables for the flask app/
    Using envoironment variables where available otherwise
    create the config variable if not done
    
    """
    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess.. NA NA nana BOO BOO'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEPLOY_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # turn off update messages from sql