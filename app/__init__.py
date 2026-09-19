
from flask import Flask
from dotenv import load_dotenv

from app.routes import main
from app.pages import pages
from config import config
from app.database import init_db

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config["development"])
    app.json.ensure_ascii = False
    with app.app_context():
        init_db()

    app.register_blueprint(main)
    app.register_blueprint(pages)

    return app