def print_with_even_index(items: list):
    """Печать элементов с четными индексами"""
    length = len(items)
    if length == 0:
        return

    return print_even_index(items, 0)


def print_even_index(items, index):
    if index > (len(items) - 1):
        return

    is_even = index % 2
    if is_even == 0:
        print(items[index])

    return print_even_index(items, index + 1)
