from config import app, db
from faker import Faker
from hashlib import sha256

from base.factory import Factory
from app.models.user_model import UserModel

class UserFactory(Factory):
    faker = Faker()
        
    def create(self):
        with app.app_context():
            user = UserModel(
                username=self.faker.user_name(), 
                email=self.faker.email(), 
                password=sha256(self.faker.password().encode('utf-8')).hexdigest(), 
                role=1
            )
            db.session.add(user)
            db.session.commit()