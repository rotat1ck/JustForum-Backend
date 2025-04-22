from base.migration import Migration
from config import app, db

class Migrate(Migration):
    def create(self):
        with app.app_context():
            db.create_all()
            
    def drop(self):
        with app.app_context():
            db.drop_all()