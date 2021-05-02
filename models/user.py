import sqlite3
from db import db

class UserModel(db.Model):
    TABLE_NAME = 'users'
    
    __tablename__ = 'users'
    id= db.Column(db.Integer,primary_key=True)
    username= db.Column(db.String(80))
    password= db.Column(db.String(50))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, user_name):
        return UserModel.query.filter_by(username=user_name).first()

    @classmethod
    def find_by_id(cls, user_id):
        return UserModel.query.filter_by(id=user_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()