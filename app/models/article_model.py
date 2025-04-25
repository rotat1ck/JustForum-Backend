from base.model import Model
from config import db

class ArticleModel(Model):
    __tablename__ = 'articles' # название таблицы
    id = db.Column(db.Integer, primary_key=True) # id статьи
    user_id = db.Column(db.Integer, unique=False, nullable=False) # id автора, юзера
    category_id = db.Column(db.Integer, unique=True, nullable=False) # id категории
    title = db.Column(db.String(50), nullable=False) # название статьи
    description = db.Column(db.String(200), nullable=True) # описание статьи
    content = db.Column(db.Text, nullable= False) # контент статьи
    created_up = db.Column(db.DateTime, nullable=False) # дата создания статьи
    updated_ap = db.Column(db.DateTime, nullable=False) # дата редактирования статьи