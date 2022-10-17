
def length_list(items: list) -> int:
    """Расчет длины списка"""
    try:
        items.pop()
    except IndexError:
        return 0

    return 1 + length_list(items)
