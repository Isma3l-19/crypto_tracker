# Cryptocurrency Tracker

A simple cryptocurrency tracker built with **Python** and **Flask** that retrieves and displays live cryptocurrency data from the **CoinMarketCap API**. Users can dynamically choose which cryptocurrencies to track, and the app leverages caching to reduce API calls.

## Features

- Fetch live cryptocurrency prices (e.g., Bitcoin, Ethereum) using the CoinMarketCap API.
- Dynamic cryptocurrency selection: users can enter symbols to track.
- Basic caching (5 minutes) to minimize API requests.
- Displays additional data, such as 24-hour percentage change and trading volume.
- API keys and sensitive data are securely stored in a `.env` file.

## Project Structure

```plaintext``
crypto_tracker/
│
├── app/
│   ├── __init__.py           # Initializes the Flask app and cache
│   ├── routes.py             # Defines app routes and views
│   ├── config.py             # Configuration settings (optional use for scalability)
│   ├── templates/
│   │   └── index.html        # HTML template for the main page
│   └── services/
│       └── crypto_service.py # Service for API calls and caching
│
├── .env                      # Environment file for API keys
├── requirements.txt          # Project dependencies
└── run.py                    # Entry point to run the Flask app

## Getting Started


### Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **CoinMarketCap API Key**: Sign up at [CoinMarketCap](https://coinmarketcap.com/api/) and obtain an API key.

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Isma3l-19/crypto_tracker.git
   cd crypto_tracker

## Installation

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt

### Set up the `.env` file

Create a `.env` file in the project root and add your CoinMarketCap API key:

```plaintext
API_KEY="your_coinmarketcap_api_key_here"
