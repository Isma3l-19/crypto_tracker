import requests
from flask import current_app

def get_crypto_data():
    url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"
    params = {
        "symbol": "BTC,ETH", # Symbols of the crypto currencies you want to track
        "convert": "USD"
    }
    headers = {
        "X-CMC_PRO_API_KEY": current_app.config['API_KEY']
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status() # Raises exceptions for HTTP errors
        data = response.json()

        # Extract relevant data for display
        crypto_data = {
            "bitcoin": {
                "usd": data["data"]["BTC"]["quote"]["USD"]["price"]
            },
            "ethereum": {
                "usd": data["data"]["ETH"]["quote"]["USD"]["price"]
            }
        }
        return crypto_data
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Failed to fetch data: {e}"}