def validate_side(side:str):

    if side.upper() not in ["BUY","SELL"]:
        raise ValueError("Side Must Be BUY or Sell Side")
    return side.upper()

def validate_order_type(order_type: str):
    order_type = order_type.upper()

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order must be MARKET or LIMIT")

    return order_type


def validate_quantity(quantity :float):
    if quantity <= 0:
        raise ValueError("Quantity Must be Above 0")
    return quantity

def validate_price(price, order_type):
    if order_type == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT orders")
        if float(price) <= 0:
            raise ValueError("Price must be greater than 0")
        return float(price)

    # For MARKET orders, ignore price
    return None

