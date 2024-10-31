import requests
from flask import current_app
from flask_caching import Cache

# Initialize cache for this module
cache = Cache(config={'CACHE_TYPE': 'simple'})

def init_cache(app):
    """Initialize cache with the Flask app context."""
    cache.init_app(app)

# Cache data for 5 minutes
@cache.memoize(timeout=300)
def get_crypto_data(symbols):
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    params = {
        "symbol": symbols,
        "convert": "USD"
    }
    headers = {
        "X-CMC_PRO_API_KEY": current_app.config['API_KEY']
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status() # Raises exceptions for HTTP errors
        data = response.json()

        # Extract relevant data for each symbol in the list
        crypto_data = {
            symbol.lower(): {
                "usd": data["data"][symbol]["quote"]["USD"]["price"],
                "percent_change_24h": data["data"][symbol]["quote"]["USD"]["percent_change_24h"],
                "volume_24h": data["data"][symbol]["quote"]["USD"]["volume_24h"]
            } for symbol in symbols.split(",")
        }
        return crypto_data
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch data: {e}"}