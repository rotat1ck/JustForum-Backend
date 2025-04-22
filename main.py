from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from config.config import Config
import os

app = Flask(__name__)
db = SQLAlchemy()

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, Config.DATABASE)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'

    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(port=Config.PORT, host=Config.APP_URL)