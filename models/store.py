import sqlite3

from db import db


class StoreModel(db.Model):
    """ A model for an store object. Extends SQLAlchemy Model object

    Attributes:
        name (str): The name of the StoreModel instance.

    Class Methods:
        find_by_name: Takes the arguement 'name' and performs a GET query on the DB to determine
            if the StoreModel is present.

    Methods:
        json: Returns the StoreModel attributes in JSON format
        save_to_db: upserts data (StoreModel) into the DB.
        delete_from_db: deletes data (StoreModel) from DB.
    """
    # DB ORM fields
    __tablename__ = 'stores'

    # Attributes MUST match the DB model properties, except for id
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # Many to one relationship (Store --> Items)
    # When lazy=dynamic is used, self.items becomes a query builder
    items = db.relationship('ItemModel', lazy='dynamic')
    
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def find_by_name(cls, name):
        # refactored SQLAlchemy ORM
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        # refactored SQLAlchemy ORM to upsert
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        # refactored SQLAlchemy ORM
        db.session.delete(self)
        db.session.commit()

    def json(self):
        # List Comprehension; provides JSON for all items related to
        # this store instance
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}