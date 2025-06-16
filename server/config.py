import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://motioncode:Jesusismyno.1@localhost:5432/pizza_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
