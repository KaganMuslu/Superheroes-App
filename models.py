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
    hero_id = db.Column(db.Integer)
    name = db.Column(db.String)
    full_name = db.Column(db.String)
    image_url = db.Column(db.String)
    intelligence = db.Column(db.Integer)
    strength = db.Column(db.Integer)
    speed = db.Column(db.Integer)
    durability = db.Column(db.Integer)
    power = db.Column(db.Integer)
    combat = db.Column(db.Integer)


class SUP_User_Heroes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    hero_id = db.Column(db.Integer)
    hero_get_date = db.Column(db.DateTime(), default=func.now())

