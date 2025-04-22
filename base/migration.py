from abc import ABC, abstractmethod

class Migration(ABC):
    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def drop(self):
        pass
