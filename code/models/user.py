import sqlite3

from db import db


class UserModel(db.Model):
    """A class representing the model for a User in data. Extends SQLAlchemy model object

    Attributes:
        id (int): The user's id in localstorage data (from security.py)
        username (str): The user's username in localstorage data (from security.py)
        password (str): The user's password in localstorage data (from secuirty.py)

    Methods:
        find_by_username: queries the sqlite DB for a user, using the 'username' argument as a 
            value for the query with parameter replacement. Returns the user object if found,
            otherwise returns None.
        find_by_id: queries the sqlite DB for a user, using the 'id' argument as a 
            value for the query with parameter replacement. Returns the user object if found,
            otherwise returns None.
    """
    # DB ORM fields
    __tablename__ = 'users'

    # Attributes MUST match the DB model properties
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,)) # single value tuple needs a commma
        row = result.fetchone() # gets first result from query
        if row:
            user = cls(*row) # row unpacking
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (id,)) # single value tuple needs a commma
        row = result.fetchone() # gets first result from query
        if row:
            user = cls(*row) # row unpacking
        else:
            user = None

        connection.close()
        return user