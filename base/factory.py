from abc import ABC, abstractmethod

class Factory(ABC):
    @abstractmethod
    def create_object(self):
        pass