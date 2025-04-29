# registration
from base.controller import Controller
from app.requests.auth.register_request import RegisterRequest
from flask import jsonify, request

class AuthController(Controller):
    @staticmethod
    def register():
        reqvalid = RegisterRequest()
        res = reqvalid.validate(request.get_json())
        if res["is_failure"] != False:
            key, value = list(res["errors"][0].items())[0]
            return jsonify({key: value}), 400
        
        return jsonify({"message": "молодец"}), 200