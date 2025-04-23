import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.migrations.migrate import Migrate
from database.seeders.user_seeder import UserSeeder

# миграции будут производиться только на таблицах чьи модели импортированы
from app.models.user_model import UserModel # также можно вместо класса импортировать *

if __name__ == '__main__':
    migrate = Migrate()
    migrate.drop()
    migrate.create()
    
    seeder = UserSeeder()
    seeder.seed_object(10)