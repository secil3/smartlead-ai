from flask import Blueprint, render_template

pages = Blueprint("pages", __name__)


@pages.route("/")
def home():
    return render_template("index.html")

@pages.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

