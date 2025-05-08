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
            not_validated["errors"].append({"error": "Username is required"})
            
        #email
        email = params.get("email")
        email_validated = self.email(email)
        if email_validated["is_failure"]:
            not_validated["errors"].append({"error": email_validated["error"]})
            
        #password
        password = params.get("password")
        password_validated = self.password(password)
        if password_validated["is_failure"]:
            not_validated["errors"].append({"error": password_validated["error"]})
            
        #return
        if len(not_validated["errors"]) > 0:
            not_validated["is_failure"] = True
        
        return not_validated