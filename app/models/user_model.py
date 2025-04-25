from base.model import Model
from config import db

class UserModel(Model):
    __tablename__ = 'users' # название таблицы
    id = db.Column(db.Integer, primary_key = True) # id пользователя
    username = db.Column(db.String(80), nullable = False) # имя пользователя
    email = db.Column(db.String(120), unique=True, nullable = False) # email пользователя
    password = db.Column(db.String(120), nullable = False) # захэшированный пароль
    role = db.Column(db.Integer, nullable = False) #роль пользователя (юзер, админ)
    email_verification = db.Column(db.String(80), nullable = True) # верификация email
    is_banned = db.Column(db.Boolean, nullable = False, default = False) # статус блокировки пользователя