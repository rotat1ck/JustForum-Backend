from base.model import Model
from config import db

class CommentModel(Model):
    __tablename__ = 'comments' # название таблицы
    id = db.Column(db.Integer, primary_key=True) # id комментария
    user_id = db.Column(db.Integer, unique=False, nullable=False) # id автора комментария
    article_id = db.Column(db.Integer, unique=False, nullable=False) # id статьи
    content = db.Column(db.String(200), nullable=False) # содержание комментария
    created_at = db.Column(db.DateTime, nullable=False) # дата создания комментария
    updated_at = db.Column(db.DateTime, nullable=False) # дата редактирования комментария