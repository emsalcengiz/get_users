from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass

db = SQLAlchemy()

@dataclass
class Job(db.Model):
    id : int
    userid: str
    location: str
    jobcreatedate: str
    jobdate: str
    jobstatus: str
    revenue: str
    servicename: str
    jobidentifier: int
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(255))
    location = db.Column(db.String(255))
    jobcreatedate = db.Column(db.String(255))
    jobdate = db.Column(db.String(255))
    jobstatus = db.Column(db.String(255))
    jobidentifier = db.Column(db.Integer)
    revenue = db.Column(db.String(255))
    servicename = db.Column(db.String(255))
    
    def __repr__(self):
        return f'<Jobs userid={self.userid}, location={self.location}>'
