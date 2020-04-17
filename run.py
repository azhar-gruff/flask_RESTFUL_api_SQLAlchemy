from app import app
from db import db

# created to avoid circular import error
# ===== Run App ====
db.init_app(app)

# ===== DB Creation =====
@app.before_first_request # tells flask to run the following function first
def create_tables():
    db.create_all()