def difference_squares(range_end: int = 100) -> int:
    sum_numbers = range_end * (range_end + 1) // 2
    sum_squares = range_end * (range_end + 1) * (2 * range_end + 1) // 6
    return sum_numbers**2 - sum_squares

print(difference_squares())