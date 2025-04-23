from base.factory import Factory
from config import db
from app.models.user_model import UserModel

class UserFactory(Factory):
    def create_object(self, user_object):
        db.session.add(user_object)
        db.session.commit()