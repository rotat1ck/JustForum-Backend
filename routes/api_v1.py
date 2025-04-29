from flask import Blueprint
from app.controllers.user_controller import UserController
from app.controllers.auth_controller import UserController

user_bp = Blueprint('user', __name__)
user_bp.add_url_rule('/test', view_func=UserController.test, methods=['GET'])
