import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.migrations.migrate import Migrate
from database.seeders.user_seeder import UserSeeder
from database.seeders.article_seeder import ArticleSeeder
from database.seeders.comment_seeder import CommentSeeder

# миграции будут производиться только на таблицах чьи модели импортированы
from app.models.user_model import UserModel # также можно вместо класса импортировать *
from app.models.article_model import ArticleModel # таблица статей
from app.models.category_model import CategoryModel # таблица категорий
from app.models.comment_model import CommentModel # таблица комментариев

if __name__ == '__main__':
    migrate = Migrate()
    migrate.drop()
    migrate.create()
    
    user_seeder = UserSeeder()
    user_seeder.seed(10)
    
    article_seeder = ArticleSeeder()
    article_seeder.seed(10)
    
    comment_seeder = CommentSeeder()
    comment_seeder.seed(10)