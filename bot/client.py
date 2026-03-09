import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

TESTNET_URL = "https://testnet.binancefuture.com/fapi"


def get_client():

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("API keys missing. Please configure .env")

    client = Client(api_key, api_secret)

    client.FUTURES_URL = TESTNET_URL

    return client
