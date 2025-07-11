from flask_login import UserMixin
from app.extensions import db
from datetime import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    function = db.Column(db.String(120))
    permission = db.Column(db.String(50))
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    password = db.Column(db.String(120))

class Attendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(100), nullable=False)
    date_worked = db.Column(db.Date, nullable=False)
    hours_worked = db.Column(db.Float, nullable=False, default=8.0)
