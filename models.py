from . import db

class Human(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name: str = db.Column(db.String(30), index=True, unique = False)
    sec_name: str = db.Column(db.String(50), index=True, unique = False)
    photo: str = db.Column(db.String(300), index=True, unique = False)
    gender: str = db.Column(db.String(10), index=True, unique = False)
    age: int = db.Column(db.Integer(200), index=True, unique = False)
    country: str = db.Column(db.String(20), index=True, unique = False)
    bio: str = db.Column(db.String(15000), index=True, unique = False)
