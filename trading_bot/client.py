import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv()
BASE_URL = "https://testnet.binancefuture.com/fapi"

class BinaceFuturesClient:
    def __init__(self):
        api_key = os.getenv("BINANCE_API_KEY")
        secret_key = os.getenv("BINANCE_SECRET_KEY")

        self.client = Client(api_key ,secret_key)
        self.client.FUTURES_URL = BASE_URL
    
    def place_order(self, **params):
        return self.client.futures_create_order(**params)

