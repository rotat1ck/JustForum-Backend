from config import app, db
from time import time
from random import randint

from base.factory import Factory
from app.models.rating_model import RatingModel

class RatingFactory(Factory):
    def create(self, rating_object):
        db.session.add(rating_object)
        db.session.commit()

    def create_secure(self):
        with app.app_context():
            timestamp = int(time())
            rating_object = RatingModel(
                user_id = randint(1, 10), 
                article_id = randint(1, 10),
                value = randint(1, 5),
                created_at = timestamp,
                updated_at = timestamp
            )
            
            check_object = RatingModel.query.filter_by(
                user_id = rating_object.user_id, 
                article_id = rating_object.article_id
            ).first()
            
            if check_object is None:
                self.create(rating_object)