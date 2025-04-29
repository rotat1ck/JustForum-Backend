# registration
from base.controller import Controller
from flask import jsonify, request
from app.requests.auth.login_request import LoginRequest

class AuthController(Controller):
    @staticmethod
    def register():
        LoginRequest().validate()
        