from .client import BinaceFuturesClient
from .logging_config import setup_logger

logger = setup_logger()
client = BinaceFuturesClient()

def place_futures_order(symbol ,side ,order_type ,quantity,price = None ):
    try:
        parms ={
            "symbol": symbol.upper(),
            "side": side,
            "type": order_type,
            "quantity": quantity
        }
        if order_type == "LIMIT":
         parms["price"] = price
         parms ["timeInforce"] = "GTC"
    
        logger.info(f"Requests: {parms}")
    
        response = client.place_order(**parms)

        logger.info(f"Response : {response}")

        return response
    except Exception as e:
       logger.error(f"Error Placing the Order: {str(e)}")
       raise
