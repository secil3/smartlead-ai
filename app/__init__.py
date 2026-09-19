import os
from flask import Flask
from dotenv import load_dotenv

from app.routes import main
from app.pages import pages

load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ["FLASK_SECRET_KEY"]
    app.json.ensure_ascii = False

    app.register_blueprint(main)
    app.register_blueprint(pages)

    return app