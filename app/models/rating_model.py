from base.model import Model
from config import db

class RatingModel(Model):
    __tablename__ = 'ratings' # название таблицы
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # id рейтинга
    user_id = db.Column(db.Integer, unique=False, nullable=False) # id пользователя, поставившего оценку
    article_id = db.Column(db.Integer, unique=False, nullable=False) # id статьи
    value = db.Column(db.Integer, nullable=False) # значение рейтинга
    created_up = db.Column(db.DateTime, nullable=False) # дата создания оценки
    updated_ap = db.Column(db.DateTime, nullable=False) # дата редактирования оценки