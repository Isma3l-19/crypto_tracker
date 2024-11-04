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
        response.raise_for_status()  # Raises exceptions for HTTP errors
        data = response.json()

        # Check for specific CoinMarketCap errors
        if 'status' in data and data['status']['error_code'] != 0:
            return {"error": data['status']['error_message']}

        # Extract relevant data for each symbol in the list
        crypto_data = {
            symbol.lower(): {
                "usd": data["data"][symbol]["quote"]["USD"]["price"],
                "percent_change_24h": data["data"][symbol]["quote"]["USD"]["percent_change_24h"],
                "volume_24h": data["data"][symbol]["quote"]["USD"]["volume_24h"],
                "market_cap": data["data"][symbol]["quote"]["USD"]["market_cap"],
                "circulating_supply": data["data"][symbol]["circulating_supply"]
            } for symbol in symbols.split(",")
        }
        return crypto_data

    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch data: {e}"}

def get_historical_data(symbol):
    """Mock function to return historical data for a cryptocurrency symbol."""
    # Example mock data
    data = {
        "BTC": {
            "dates": ["2023-10-24", "2023-10-25", "2023-10-26", "2023-10-27", "2023-10-28", "2023-10-29", "2023-10-30"],
            "prices": [30000, 30500, 31000, 29500, 32000, 31500, 33000]
        },
        "ETH": {
            "dates": ["2023-10-24", "2023-10-25", "2023-10-26", "2023-10-27", "2023-10-28", "2023-10-29", "2023-10-30"],
            "prices": [1800, 1850, 1820, 1790, 1900, 1925, 1950]
        }
    }
    return data.get(symbol.upper(), {"dates": [], "prices": []})
