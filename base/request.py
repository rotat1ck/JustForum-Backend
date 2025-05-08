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
        
        # проверка существования
        if password is None:
            not_validated["is_failure"] = True
            not_validated["error"] = "Password is required"
        
        # проверка по паттерну
        elif re.match(pattern, password) is None:
            not_validated["is_failure"] = True
            not_validated["error"] = "Entered password doesn't satisfy the requirements"
        
        return not_validated
    
    @staticmethod
    def email(email):
        not_validated = {
            "error": [],
            "is_failure": False
        }
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        
        # проверка существования
        if email is None:
            not_validated["is_failure"] = True
            not_validated["error"] = "Email is required"
        
        # проверка по паттерну
        elif re.match(pattern, email) is None:
            not_validated["is_failure"] = True
            not_validated["error"] = "Entered email doesn't satisfy the requirements"

        return not_validated