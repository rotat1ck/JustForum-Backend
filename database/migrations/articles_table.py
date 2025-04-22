from base.migration import Migration

class ArticlesTable(Migration):
    def create(self):
        self.create_table('articles', columns={ 
            'id': 'INTEGER PRIMARY KEY', 
            'title': 'TEXT', 
            'content': 'TEXT', 
            'created_at': 'DATETIME DEFAULT CURRENT_TIMESTAMP' 
        })