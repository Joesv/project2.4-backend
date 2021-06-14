from app import app
from app.config import Config

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=Config.PORT, debug=True)