from flask import Blueprint, render_template, request
from .services.crypto_service import get_crypto_data, get_historical_data

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    symbols = "BTC,ETH"  # Default symbols
    if request.method == "POST":
        symbols = request.form.get("symbols", "BTC,ETH").replace(" ", "")  # Remove spaces

    crypto_data = get_crypto_data(symbols)
    
    # Fetch historical data for the first symbol in the list
    first_symbol = symbols.split(",")[0].strip()
    historical_data = get_historical_data(first_symbol)
    
    return render_template("index.html", data=crypto_data, historical_data=historical_data, symbol=first_symbol.upper())
