from flask import Blueprint, render_template
from .services.crypto_service import get_crypto_data

main = Blueprint("main", __name__)

@main.route("/")
def index():
    crypto_data = get_crypto_data()
    return render_template("index.html", data=crypto_data)