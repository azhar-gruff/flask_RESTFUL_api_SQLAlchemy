import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identify
from resources.user import UserRegister # refactored for modules
from resources.item import Item, ItemList # refactored for modules
from resources.store import Store, StoreList

# ==== Server =====
app = Flask(__name__)
# refactored to use environment variable, or sqlite if the environment
# variable is not present
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'thisisasecretkey' # NOTE change for production
api = Api(app)

# === Security ===
jwt = JWT(app, authenticate, identify) # creates /auth endpoint

# ===== Endpoints =====
# add the class, along with the URL
api.add_resource(Store, '/store/<string:name>') # http//127.0.0.1:5000/store/walmart
api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/item/cheese
api.add_resource(StoreList, '/stores') # http//127.0.0.1:5000/stores
api.add_resource(ItemList, '/items') # http//127.0.0.1:5000/items
api.add_resource(UserRegister, '/register') # http://127.0.0.1:5000/register

# ===== Server =====
# only runs if this file is the entry point for the application. This 
# does not run if this file is imported
if __name__ == '__main__':
    from db import db
    db.init_app(app)

    app.run(port=5000, debug=True)