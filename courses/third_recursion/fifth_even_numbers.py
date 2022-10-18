
def print_even_numbers(items: list):
    """Печать четных значений из списка"""
    if len(items) == 0:
        return

    item = items.pop(0)
    is_even = item % 2
    if is_even == 0:
        print(item)

    return print_even_numbers(items)

