import sqlite3

from db import db


class UserModel(db.Model):
    """A class representing the model for a User in data. Extends SQLAlchemy model object

    Attributes:
        username (str): The UserModel instance username in the DB.
        password (str): The UserModel instance password in the DB.

    Class Methods:
        find_by_username: queries the sqlite DB for a UserModel, using the 'username' argument as a 
            value for the query with parameter.
        find_by_id: queries the sqlite DB for a Model, using the 'id' argument as a 
            value for the query with parameter.

    Methods:
        save_to_db: upserts data (UserModel) into the DB.
    """
    # DB ORM fields
    __tablename__ = 'users'

    # Attributes MUST match the DB model properties, except for is
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        # refactored SQLAlchemy ORM
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, id):
        # refactored SQLAlchemy ORM
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        # SQL ALchemy
        db.session.add(self)
        db.session.commit()