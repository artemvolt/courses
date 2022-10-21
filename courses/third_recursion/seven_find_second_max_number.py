def find_second_max_number(items: list, max=None, second_max=None):
    """Печать четных значений из списка"""
    if len(items) == 0:
        return second_max

    current = items.pop(0)
    if max is None and second_max is None:
        max = second_max = current

    if current > max:
        second_max = max
        max = current

    if second_max < current < max:
        second_max = current

    return find_second_max_number(items, max, second_max)
