def print_with_even_index(items: list, index=0) -> int:
    """Печать элементов с четными индексами"""
    length = len(items)
    if length == 0:
        return

    if length < (index + 1):
        return

    is_even = index % 2
    if is_even == 0:
        print(items[index])

    return print_with_even_index(items, index + 1)
