from base.factory import Factory
from config import db
from app.models.comment_model import CommentModel

class CommentFactory(Factory):
    def create(self, comment_object):
        db.session.add(comment_object)
        db.session.commit()