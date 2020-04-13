import sqlite3

from db import db


class ItemModel(db.Model):
    """ A model for an Item object. Extends SQLAlchemy Model object

    Attributes:
        name (str): The name of the item
        price (decimal): The cost of an item

    Class Methods:
        find_by_name: Takes the arguement 'name' and performs a GET query on the DB to determine
            if the item is present.

    Methods:
        json: Returns the item model attributes in JSON format
        
        insert: Takes in an Item as an argument. Opens a stream to the DB and performs an insert
            query to add a new data piece.

        update: Takes in an Item as an argument. If the Item is not present in the DB, creates a
            new Item using the Item argument's name attribute and adds it to the DB. Otherwise, it
            updates the item in the DB that matches the provided Item argument's name attribute.
    """
    # DB ORM fields
    __tablename__ = 'items'

    # Attributes MUST match the DB model properties
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @classmethod
    def find_by_name(cls, name):
        # DB connect
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        # query
        query = "SELECT * FROM items WHERE name = ?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return cls(*row) # argument unpacking (row[0] = name, row[1] price)

    def insert(self):
        # DB Connect
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        # query
        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (self.name, self.price))

        connection.commit()
        connection.close()

    def update(self):
        # DB Connect
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        # query
        query = "UPDATE items SET price = ? WHERE name = ?"
        cursor.execute(query, (self.price, self.name))

        connection.commit()
        connection.close()

    def json(self):
        return {'name': self.name, 'price': self.price}