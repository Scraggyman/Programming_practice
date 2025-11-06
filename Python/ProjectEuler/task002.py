def even_fibonacci_sum(limit: int = 1_000_000) -> int:
    """
    """
    a, b = 1, 2
    total = 0
    while b <= limit:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total

print(f"Сумма четных чисел из ряда Фибоначчи 4 000 000:", even_fibonacci_sum(4_000_000))