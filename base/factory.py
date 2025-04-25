from abc import ABC, abstractmethod

class Factory(ABC):
    @abstractmethod
    def create(self):
        pass