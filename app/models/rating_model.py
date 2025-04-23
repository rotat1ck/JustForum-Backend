from base.model import Model
from config import db

class RatingModel(Model):
    __tablename__ = 'rating' # название таблицы
    id = db.Column(db.Integer, primary_key=True) # id рейтинга
    user_id = db.Column(db.String(80), unique=True, nullable=False) # id пользователя, поставившего оценку
    article_id = db.Column(db.String(80), unique=True, nullable=False) # id статьи
    value = db.Column(db.Integer, nullable=False) # значение рейтинга
    created_at = db.Column(db.String(10), nullable=False) # дата создания рейтинга