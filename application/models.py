# Models for future user login
from application.db import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=70), nullable=False)
    items = db.relationship("Entry")


class Entry(db.Model):
    __tablename__ = 'entries'

    id = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(length=70), nullable=False)
    weather = db.Column(db.String(length=70), nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    temp = db.Column(db.Float, nullable=False)
    owner = db.Column(db.Integer, db.ForeignKey("users.id"))
