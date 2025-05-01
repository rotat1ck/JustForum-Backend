from abc import ABC, abstractmethod
import re

class Request(ABC):
    @abstractmethod
    def validate(self):
        pass
    
    @staticmethod
    def password(password):
        not_validated = {
            "error": None,
            "is_failure": False
        }
        pattern = r"^.{8,}$"
        
        if re.match(pattern, password) is None:
            not_validated["is_failure"] = True
            not_validated["error"] = "Entered password doesn't satisfy the requirements"
            return not_validated
        
        return not_validated
    
    @staticmethod
    def email(email):
        not_validated = {
            "error": [],
            "is_failure": False
        }
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        
        #check
        if re.match(pattern, email) is None:
            not_validated["is_failure"] = True
            not_validated["error"] = "Entered email doesn't satisfy the requirements"
            return not_validated

        return not_validated