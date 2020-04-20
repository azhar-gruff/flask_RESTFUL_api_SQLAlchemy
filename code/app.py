from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identify
from resources.user import UserRegister # refactored for modules
from resources.item import Item, ItemList # refactored for modules
from resources.store import Store, StoreList

# ==== Server =====
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' # can be any DB, not just sqlite
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'thisisasecretkey' # NOTE change for production
api = Api(app)

# ===== DB Creation =====
@app.before_first_request # tells flask to run the following function first
def create_tables():
    db.create_all()

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

    if app.config['DEBUG']:
        @app.before_first_request
        def create_Tables():
            db.create_all()

    app.run(port=5000)