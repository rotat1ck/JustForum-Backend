from config import app
from faker import Faker
from hashlib import sha256

from base.seeder import Seeder
from database.factories.user_factory import UserFactory
from app.models.user_model import UserModel

class UserSeeder(Seeder):
    faker = Faker()
    
    def seed(self, iterations):
        with app.app_context():
            for _ in range(iterations):
                user = UserModel(
                    username=self.faker.user_name(), 
                    email=self.faker.email(), 
                    password=sha256(self.faker.password().encode('utf-8')).hexdigest(), 
                    role=1
                )
                UserFactory().create(user)