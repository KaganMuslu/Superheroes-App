from app import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class SUP_Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    create_date = db.Column(db.DateTime(timezone=True), default=func.now())


class SUP_Superheroes(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String)
    full_name = db.Column(db.String, default=name)

    image = db.Column(db.String)

    app_gender = db.Column(db.String)
    app_race = db.Column(db.String, default="-")
    app_height = db.Column(db.String)
    app_weight = db.Column(db.String)
    app_eyeColor = db.Column(db.String)
    app_hairColor = db.Column(db.String)

    bio_alterEgos = db.Column(db.String)
    bio_aliases = db.Column(db.String)
    bio_placeOfBirth = db.Column(db.String)
    bio_firstAppearance = db.Column(db.String)
    bio_publisher = db.Column(db.String, default="-")
    bio_alignment = db.Column(db.String)

    work_occupation = db.Column(db.String)
    work_base = db.Column(db.String)
    con_groupAffiliation = db.Column(db.String)
    con_relatives = db.Column(db.String)

    stat_intelligence = db.Column(db.Integer)
    stat_strength = db.Column(db.Integer)
    stat_speed = db.Column(db.Integer)
    stat_durability = db.Column(db.Integer)
    stat_power = db.Column(db.Integer)
    stat_combat = db.Column(db.Integer)


class SUP_User_Superheroes(db.Model):
    id = db.Column(db.Integer, primary_key=True, index=True)
    user_id = db.Column(db.Integer)
    superhero_id = db.Column(db.Integer)
    hero_get_date = db.Column(db.DateTime(timezone=True), default=func.now())
