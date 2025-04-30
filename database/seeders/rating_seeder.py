from base.seeder import Seeder
from database.factories.rating_factory import RatingFactory

class RatingSeeder(Seeder):
    def seed(self, iterations):
        for _ in range(iterations):
            RatingFactory().create_secure()