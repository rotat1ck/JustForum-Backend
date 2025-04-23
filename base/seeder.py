from abc import ABC, abstractmethod

class Seeder(ABC):
    @abstractmethod
    def seed_object(self, iterations):
        pass