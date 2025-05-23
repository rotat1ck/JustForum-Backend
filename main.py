from config import app
from config.config import Config
from config.app import *

if __name__ == '__main__':
    App().init_api_routes()
    app.run(port=Config.PORT, host=Config.APP_URL)