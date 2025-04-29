from base.seeder import Seeder
from database.factories.article_factory import ArticleFactory

class ArticleSeeder(Seeder):
    def seed(self, iterations):
        for _ in range(iterations):
            ArticleFactory().create()