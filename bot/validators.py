def validate_symbol(symbol):
    return symbol.upper()


def validate_side(side):
    side = side.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    return side


def validate_order_type(order_type):
    order_type = order_type.upper()

    valid_types = ["MARKET", "LIMIT", "STOP"]

    if order_type not in valid_types:
        raise ValueError(f"Order type must be one of {valid_types}")

    return order_type
