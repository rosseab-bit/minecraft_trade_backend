from app.data.items_values import values
# comment example
def convert_items(source: str, target: str, amount: float):
    if source not in values or target not in values:
        return None

    diamonds = amount * values[source]
    result = diamonds / values[target]

    return {
        "source_item": source,
        "target_item": target,
        "source_amount": amount,
        "result_amount": round(result, 3),
        "diamond_equivalent": round(diamonds, 3)
    }
