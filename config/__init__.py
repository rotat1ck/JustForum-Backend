from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
import os

app = Flask("JustForum-Backend")
db = SQLAlchemy()

current_dir = os.path.dirname(os.path.abspath(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(current_dir, '..', Config.DATABASE)}'
    
db.init_app(app)