from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    """Flask RESTful store (resource) that performs HTTP requests
    Static Attributes:
        parser (obj): Instance of the flask_restful RequestParser class. Allows for validations on
            request bodies from HTTP requests (specifically in JSON).
    
    Methods:
        get: Retrieves an store from the DB using the 'name' argument provided in the URL string.
            Uses the class method find_by_name to search the DB. This requires authentication.

        post: Adds a new store to the DB using the 'name' argument provided in the URL string. Adds
            a 'price' key/value pair supplied by the HTTP request JSON body. Uses find_by_name to
            check for the presence of the store.

        delete: Deletes an store the DB using the 'name argument provided in the URL string. If no
            store found, responds with appropriates JSON message.
    """
    def get(self, name):
        store = StoreModel.find_by_name(name)
         # data presence check
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    def post(self, name):
         # data presence check
        if StoreModel.find_by_name(name):
            return {'message': "A store with name '{}' already exists".format(name)}, 400

        store = StoreModel(name)

        # try/except block for potential DB insert failure
        try:
            store.save_to_db()
        except:
            return {'message': 'An error occured while creating the store.'}, 500 # internal server error

        return store.json(), 201 # Http status for created

    def delete(self, name):
        store = StoreModel.find_by_name(name)
         # data presence check
        if store:
            store.delete_from_db()

            return {'message': 'Store deleted'}
        return {'message': 'Store not found'}, 404


class StoreList(Resource):
    """This class generates a list of items (StoreModel class) from the database
    
    Methods:
        get: Queries the database for all stores and returns a list of stores (StoreModel class).
    """
    def get(self):
        # list comprehension
        return {'stores': [store.json() for store in StoreModel.query.all()]}
        # if you are using a different language with python (like JS)
        # using the map method may better a better option
        # return {'stores': list(map(lambda x: x.json(), StoreModel.query.all())}