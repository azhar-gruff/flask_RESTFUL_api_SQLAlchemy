from flask import Request
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

# resources from flask_restful allow you to create classes for API data
class Item(Resource):
    """Flask RESTful item (resource) that performs HTTP requests
    Static Attributes:
        parser (obj): Instance of the flask_restful RequestParser class. Allows for validations on
            request bodies from HTTP requests (specifically in JSON).
    
    Methods:
        get: Retrieves an item from the DB using the 'name' argument provided in the URL string.
            Uses the class method find_by_name to search the DB. This requires authentication.

        post: Adds a new item to the DB using the 'name' argument provided in the URL string. Adds
            a 'price' key/value pair supplied by the HTTP request JSON body. Uses find_by_name to
            check for the presence of the item.

        delete: Deletes an item the DB using the 'name argument provided in the URL string. If no
            item found, responds with appropriates JSON message.

        put: Updates or created a new item to the DB using the 'name' argument provided in the URL
            string, with the 'price' key/value pair supplied by the HTTP request JSON body.
    """
    parser = reqparse.RequestParser() # request body parser from flask_restful
    # data validations
    parser.add_argument('price',
        type = float,
        required = True,
        help = "This field cannot be left blank!"
    )

    # create fucntions for each HTTP method you will allow for the
    # resource

    # Need to receive from client Header: Authorization / "JWT token"
    # NOTE remove the "" from the JWT token in the header.
    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)

        # data presence check
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def post(self, name):
        # data presence check
        if ItemModel.find_by_name(name):
            return {'messsage': "An item with name '{}' already exists".format(name)}, 400

        data = self.parser.parse_args()
        
        item = ItemModel(name, data['price'])
        
        # try/except block for potential DB insert failure
        try:
            item.save_to_db()
        except:
            return {'message': 'An error occured inserting the item.'}, 500 # internal server error

        return item.json(), 201 # Http status for created

    def delete(self, name):
        # data present check
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db() # refactored with model

            return {'message': 'Item deleted'}
        return {'message': 'Item not found'}, 404

    def put(self, name):
        data = self.parser.parse_args()

        item = ItemModel.find_by_name(name)
        updated_item = ItemModel(name, data['price'])

        # refatored to check if item is present.
        if item is None:
           item = ItemModel(name, data['price'])
        else:
            item.price = data['price']

        item.save_to_db() # refactored to save with model
        return updated_item.json()


class ItemList(Resource):
    """This class generates a list of items (ItemModel class) from the database
    
    Methods:
        get: Queries the database for all items and returns a list of items (ItemModel class).
    """
    def get(self):
        # refactored with SQLAlchemy and list comprehension
        return {'items': [item.json() for item in ItemModel.query.all()]}
        # if you are using a different language with python (like JS)
        # using the map method may better a better option
        # return {'items': list(map(lambda x: x.json(), ItemModel.query.all())}