import argparse
from trading_bot.orders import place_futures_order
from trading_bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)

def main():
    
    parser = argparse.ArgumentParser(description="Binace Future TestNet Trading Bot")

    parser.add_argument("--symbol",required=True)
    parser.add_argument("--side", choices=["BUY", "SELL"], required=True)
    parser.add_argument("--type", choices=["MARKET", "LIMIT"], required=True)
    parser.add_argument("--quantity",required=True, type= float)
    parser.add_argument("--price", type= float)

    args = parser.parse_args()
    try:
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price, order_type)

        print("\nOrder Summary")
        print("---------------------------")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")
        if price:
            print(f"Price: {price}")

        response = place_futures_order(
            symbol=args.symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
        )

        print("\nOrder Response")
        print("---------------------------")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice', 'N/A')}")
        print("\n✅ Order placed successfully!")

    except Exception as e:
        print(f"\n❌ Failed: {str(e)}")


if __name__ == "__main__":
    main()
    


