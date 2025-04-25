from abc import ABC, abstractmethod

class Seeder(ABC):
    @abstractmethod
    def seed(self, iterations):
        pass