from base.model import Model
from config import db

class CommentModel(Model):
    __tablename__ = 'comment' # название таблицы
    id = db.Column(db.Integer, primary_key=True) # id комментария
    user_id = db.Column(db.String(80), unique=True, nullable=False) # id автора комментария
    article_id = db.Column(db.String(80), unique=True, nullable=False) # id статьи
    content = db.Column(db.Text, nullable=False) # содержание комментария
    created_at = db.Column(db.String(10), nullable=False) # дата создания комментария 