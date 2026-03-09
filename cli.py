import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_symbol, validate_side, validate_order_type
from bot.logging_config import setup_logging


def main():

    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:

        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)

        if order_type in ["LIMIT", "STOP"] and args.price is None:
            raise ValueError("LIMIT and STOP orders require --price")

        client = get_client()

        print("\n--- Order Request ---")
        print("Symbol:", symbol)
        print("Side:", side)
        print("Type:", order_type)
        print("Quantity:", args.quantity)
        print("Price:", args.price)

        response = place_order(
            client,
            symbol,
            side,
            order_type,
            args.quantity,
            args.price,
        )

        print("\n--- Order Response ---")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice"))

        print("\n✅ Order placed successfully!")

    except Exception as e:

        print("\n❌ Order failed")
        print("Reason:", str(e))


if __name__ == "__main__":
    main()
