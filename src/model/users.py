from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()

@dataclass
class User(db.Model):
    id : int
    userid: str
    location: str

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(255))
    location = db.Column(db.String(255))
    

    def __repr__(self):
        return f'<User userid={self.userid}, location={self.location}>'

