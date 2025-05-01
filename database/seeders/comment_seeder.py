from base.seeder import Seeder
from database.factories.comment_factory import CommentFactory

class CommentSeeder(Seeder):
    def seed(self, iterations):
        for _ in range(iterations):
            CommentFactory().create()