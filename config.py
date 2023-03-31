# API KEYS, SECRET KEYS, BASIC STRUCTURES OF ROUTING, TELLS OUR APP WHERE TO FIND ITSSELF:
import os 

basedir = os.path.abspath(os.path.dirname(__name__))

class Config(): #<---- define what config is
    FLASK_APP = os.environ.get('FLASK_APP') #<--- gets this flask variable from .env
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG') #<--- gets this flask variable from .env
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False