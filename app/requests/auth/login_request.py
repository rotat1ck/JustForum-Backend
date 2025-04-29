from base.request import Request
from flask import request, jsonify

class LoginRequest(Request):
    def validate(self):
        #username
        username = request.json.get("username")
        if username is None:
            return jsonify({"message": "Username is required"}), 400
        #email
        email = request.json.get("email")
        if email is None:
            return jsonify({"message": "Email is required"}), 400
        #password
        password = request.json.get("password")
        if password is None:
            return jsonify({"message": "Password is required"}), 400