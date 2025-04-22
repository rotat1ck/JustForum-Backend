from config import app
from config.config import Config

if __name__ == '__main__':
    app.run(port=Config.PORT, host=Config.APP_URL)