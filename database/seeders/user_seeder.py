from base.seeder import Seeder
from database.factories.user_factory import UserFactory


class UserSeeder(Seeder):
    def seed(self, iterations):
        for _ in range(iterations):
            UserFactory().create()