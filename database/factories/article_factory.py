from config import app, db
from faker import Faker
from time import time
from random import randint

from base.factory import Factory
from app.models.article_model import ArticleModel

class ArticleFactory(Factory):
    faker = Faker()

    def create(self):
        with app.app_context():
            timestamp = int(time())
            article = ArticleModel(
                user_id = randint(1, 10),
                category_id = randint(1, 5),
                title = self.faker.sentence(nb_words=6),
                content = self.faker.text(),
                created_at = timestamp,
                updated_at = timestamp
            )
            db.session.add(article)
            db.session.commit()