from app import db

class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False,unique=True)
    password = db.Column(db.String,nullable=False)


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False, unique=True)
    status = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
