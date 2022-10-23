def find_second_max_number(items: list):
    """Поиск второго максимального числа"""
    if len(items) == 0:
        return None

    current = items.pop(0)
    max = second_max = current

    return compare_current_with_max_and_second(items, max, second_max)


def compare_current_with_max_and_second(items, max, second_max):
    if len(items) == 0:
        return second_max

    current = items.pop(0)
    if current > max:
        second_max = max
        max = current

    if second_max < current < max:
        second_max = current

    return compare_current_with_max_and_second(items, max, second_max)
