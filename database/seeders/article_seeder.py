from config import app
from faker import Faker
from time import time
from random import randint

from base.seeder import Seeder
from database.factories.article_factory import ArticleFactory
from app.models.article_model import ArticleModel

class ArticleSeeder(Seeder):
    faker = Faker()
    
    def seed(self, iterations):
        with app.app_context():
            for _ in range(iterations):
                timestamp = int(time())
                article = ArticleModel(
                    user_id = randint(1, 10),
                    category_id = randint(1, 5),
                    title = self.faker.sentence(nb_words=6),
                    content = self.faker.text(),
                    created_at = timestamp,
                    updated_at = timestamp
                )
                ArticleFactory().create(article)