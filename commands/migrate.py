import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.migrations.migrate import Migrate

# миграции будут производиться только на таблицах чьи модели импортированы
from app.models.user_model import UserModel # также можно вместо класса импортировать *
from app.models.article_model import ArticleModel # таблица статей
from app.models.category_model import CategoryModel # таблица категорий
from app.models.comment_model import CommentModel # таблица комментариев
from app.models.rating_model import RatingModel # таблица оценок

if __name__ == '__main__':
    migrate = Migrate()
    migrate.drop()
    migrate.create()