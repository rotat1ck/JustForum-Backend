from . import app
from routes import api_v1

class App():
    def __init__(self):
        pass
        
    def init_api_routes(self):
        app.register_blueprint(api_v1.user_bp, url_prefix='/api/v1/user')
        app.register_blueprint(api_v1.auth_bp, url_prefix='/api/v1/auth')