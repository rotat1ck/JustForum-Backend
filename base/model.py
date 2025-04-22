from config import db

class Model(db.Model):
    __abstract__ = True