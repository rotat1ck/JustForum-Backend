from base.factory import Factory
from config import db
from app.models.rating_model import RatingModel

class RatingFactory(Factory):
    def create(self, rating_object):
        db.session.add(rating_object)
        db.session.commit()

    def create_secure(self, rating_object):
        check_object = RatingModel.query.filter_by(
            user_id = rating_object.user_id, 
            article_id = rating_object.article_id
        ).first()
        
        if check_object is None:
            self.create(rating_object)