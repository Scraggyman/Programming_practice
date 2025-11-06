def sum_of_multiples(n: int, k: int) -> int:
    """Calculate the sum of all natural numbers less than n that are multiples of k.

    Args:
        n (int): The upper limit (exclusive). Must be a positive integer.
        k (int): The multiple to sum. Must be a positive integer.

    Returns:
        int: The sum of all numbers less than n that are divisible by k.

    Examples:
        >>> sum_of_multiples(10, 3)
        18
        >>> sum_of_multiples(10, 5)
        5
    """

    p = (n - 1) // k 
    return k * p * (p + 1) // 2

n = 1000
total = sum_of_multiples(n, 3) + sum_of_multiples(n, 5) - sum_of_multiples(n, 15)
print(f"Сумма чисел от 0 до {n}, кратных 3 и 5: {total}")