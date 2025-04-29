from config import app
from faker import Faker
from time import time
from random import randint

from base.seeder import Seeder
from database.factories.comment_factory import CommentFactory
from app.models.comment_model import CommentModel

class CommentSeeder(Seeder):
    faker = Faker()
    
    def seed(self, iterations):
        with app.app_context():
            for _ in range(iterations):
                timestamp = int(time())
                comment = CommentModel(
                    user_id = randint(1, 10),
                    article_id = randint(1, 10),
                    content = self.faker.text(),
                    created_at = timestamp,
                    updated_at = timestamp
                )
                CommentFactory().create(comment)