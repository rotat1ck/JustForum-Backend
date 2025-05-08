from flask import Blueprint
from app.controllers.user_controller import UserController
from app.controllers.auth_controller import AuthController

user_bp = Blueprint('user', __name__)
user_bp.add_url_rule('/test', view_func=UserController.test, methods=['GET'])

auth_bp = Blueprint('auth', __name__)
auth_bp.add_url_rule('/register', view_func=AuthController.register, methods=["POST"])