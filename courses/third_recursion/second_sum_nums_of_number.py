
def sum_of_the_numbers_of_number(number: int) -> int:
    """Сумма чисел числа"""
    reminder_of_dividing = number % 10
    if reminder_of_dividing == 0:
        return 0

    return reminder_of_dividing + sum_of_the_numbers_of_number(number // 10)
