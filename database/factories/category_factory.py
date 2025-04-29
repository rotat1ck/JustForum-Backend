from base.factory import Factory
from config import db
from app.models.category_model import CategoryModel

class CategoryFactory(Factory):
    def create(self, category_object):
        db.session.add(category_object)
        db.session.commit()