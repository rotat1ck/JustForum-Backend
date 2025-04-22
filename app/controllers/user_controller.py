from base.controller import Controller
from flask import jsonify

class UserController(Controller):
    @staticmethod
    def test():
        return jsonify({'message': 'Blueprint and route /api/v1/user/test are working'}), 200