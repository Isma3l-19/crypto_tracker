from flask import Blueprint, render_template, request
from .services.crypto_service import get_crypto_data

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    symbols = "BTC,ETH" # Default symbols
    if request.method == "POST":
        symbols = request.form.get("symbols", "BTC,ETH").replace(" ", "")

    crypto_data = get_crypto_data(symbols)
    return render_template("index.html", data=crypto_data)