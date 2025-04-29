from base.factory import Factory
from config import db
from app.models.article_model import ArticleModel

class ArticleFactory(Factory):
    def create(self, article_object):
        db.session.add(article_object)
        db.session.commit()