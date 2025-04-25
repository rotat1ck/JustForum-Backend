from base.model import Model
from config import db

class CategoryModel(Model):
    __tablename__ = 'categories' # название таблицы
    id = db.Column(db.Integer, primary_key=True) # id категории
    title = db.Column(db.String(80), unique=True, nullable=False) # название категории