from base.factory import Factory
from config import db, app
from app.models.category_model import CategoryModel

class CategoryFactory(Factory):
    def create(self, category_object):
        with app.app_context:
            db.session.add(CategoryModel(
                title = "Свободная"
            ))
            db.session.add(CategoryModel(
                title = "Конспирология"
            ))
            db.session.add(CategoryModel(
                title = "Эзотерика"
            ))
            db.session.add(CategoryModel(
                title = "Здоровье"
            ))
            db.session.add(CategoryModel(
                title = "Путешествия"
            ))
            db.session.add(CategoryModel(
                title = "Мудак ли я?"
            ))
            db.session.add(CategoryModel(
                title = "Слушаем и не осуждаем"
            ))
            db.session.add(CategoryModel(
                    title = "Слушаем и осуждаем"
            ))

            db.session.commit()
        