from faker import Faker
from time import time
from random import randint
from config import db, app

from base.factory import Factory
from app.models.comment_model import CommentModel

class CommentFactory(Factory):
    faker = Faker()
    
    def create(self):
        with app.app_context():
            timestamp = int(time())
            comment = CommentModel(
                user_id = randint(1, 10),
                article_id = randint(1, 10),
                content = self.faker.text(),
                created_at = timestamp,
                updated_at = timestamp
            )
            db.session.add(comment)
            db.session.commit()