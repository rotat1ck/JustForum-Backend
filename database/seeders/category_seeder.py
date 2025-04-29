from base.seeder import Seeder
from database.factories.category_factory import CategoryFactory

class CategorySeeder(Seeder):
    def seed(self, iterations):
        CategoryFactory().create()