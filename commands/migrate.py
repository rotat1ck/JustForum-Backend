import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from database.migrations.migrate import Migrate

# миграции будут производиться только на таблицах чьи модели импортированы
from app.models.user_model import UserModel # также можно вместо класса импортировать *

if __name__ == '__main__':
    migrate = Migrate()
    migrate.drop()
    migrate.create()