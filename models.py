from app import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class SUP_User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(20))
    register_date = db.Column(db.DateTime(timezone=True), default=func.now())


class SUP_Heroes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    full_name = db.Column(db.String)
    Intelligence = db.Column(db.Integer)
    Strength = db.Column(db.Integer)
    Speed = db.Column(db.Integer)
    Durability = db.Column(db.Integer)
    Power = db.Column(db.Integer)
    Combat = db.Column(db.Integer)


class SUP_User_Heroes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    hero_id = db.Column(db.Integer)

