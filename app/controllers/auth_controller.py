# registration
from base.controller import Controller
from app.requests.auth.register_request import RegisterRequest
from app.models.user_model import UserModel

from flask import jsonify, request
from config import db
from time import time
from hashlib import sha256

class AuthController(Controller):
    def register():
        reqvalid = RegisterRequest()
        params = request.get_json()
        res = reqvalid.validate(params)
        if res["is_failure"] != False:
            key, value = list(res["errors"][0].items())[0]
            return jsonify({key: value}), 400
        
        new_user = UserModel(
            username = params.get("username"),
            email = params.get("email"),
            password = sha256(params.get("username").encode('utf-8')).hexdigest(),
            role = 1
        )
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({"user": new_user}), 200