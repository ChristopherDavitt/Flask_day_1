import os

basedir = os.path.abspath(os.path.dirname(__file__))

# gives access to the project in any OS we find mac, pc, etc.
# allows outside files/folders to be added to the project from the base directory

class Config:
    # FLASK_ENV
    """
    Set Config variables for the flask app/
    Using envoironment variables where available otherwise
    create the config variable if not done
    
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess.. NA NA nana BOO BOO'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # turn off update messages from sql