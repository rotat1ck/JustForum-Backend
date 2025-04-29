from config import app

from base.seeder import Seeder
from database.factories.category_factory import CategoryFactory
from app.models.category_model import CategoryModel

class CategorySeeder(Seeder):
    def seed(self, iterations):
        with app.app_context():
            CategoryFactory().create(CategoryModel(
                title = "Свободная"
            ))
            CategoryFactory().create(CategoryModel(
                title = "Конспирология"
            ))
            CategoryFactory().create(CategoryModel(
                title = "Эзотерика"
            ))
            CategoryFactory().create(CategoryModel(
                title = "Здоровье"
            ))
            CategoryFactory().create(CategoryModel(
                title = "Путешествия"
            ))
            CategoryFactory().create(CategoryModel(
                title = "Мудак ли я?"
            ))
            CategoryFactory().create(CategoryModel(
                title = "Слушаем и не осуждаем"
            ))
            CategoryFactory().create(CategoryModel(
                title = "Слушаем и осуждаем"
            ))