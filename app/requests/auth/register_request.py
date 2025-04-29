from base.request import Request
from flask import request, jsonify

class RegisterRequest(Request):
    def validate(self, params):
        not_validated = {
            "errors": [],
            "is_failure": False
        }
        #username
        if params.get("username") is None:
            not_validated["is_failure"] = True
            not_validated["errors"].append({"message": "Username is required"})
        #email
        if params.get("email") is None:
            not_validated["is_failure"] = True
            not_validated["errors"].append({"message": "Email is required"})
        #password
        if params.get("password") is None:
            not_validated["is_failure"] = True
            not_validated["errors"].append({"message": "Password is required"})
        
        return not_validated