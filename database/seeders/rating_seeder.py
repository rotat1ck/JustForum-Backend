from config import app
from time import time
from random import randint

from base.seeder import Seeder
from database.factories.rating_factory import RatingFactory
from app.models.rating_model import RatingModel

class RatingSeeder(Seeder):
    def seed(self, iterations):
        with app.app_context():
            for _ in range(iterations):
                timestamp = int(time())
                # данный сидэр не подразумивает защиту от повторных оценок одного и того же поста, этим будет заниматься контроллер
                # поэтому из-за рандома один юзер может оставить две оценки на один пост
                rating = RatingModel(
                    user_id = randint(1, 10), 
                    article_id = randint(1, 10),
                    value = randint(1, 5),
                    created_at = timestamp,
                    updated_at = timestamp
                )
                
                # я решил все же сделать функцию в factory для безопастного создания
                RatingFactory().create_secure(rating)