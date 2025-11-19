import math

def sieve_of_atkin(limit: int) -> list[int]:
    if limit < 2:
        return []

    primes = [2, 3]
    sieve = [False] * (limit + 1)

    for x in range(1, int(math.sqrt(limit)) + 1):
        for y in range(1, int(math.sqrt(limit)) + 1):
            n = 4 * x**2 + y**2
            if n <= limit and n % 12 in (1, 5):
                sieve[n] = not sieve[n]
            n = 3 * x**2 + y**2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = 3 * x**2 - y**2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]

    for n in range(5, int(math.sqrt(limit)) + 1):
        if sieve[n]:
            k = n * n
            for i in range(k, limit + 1, k):
                sieve[i] = False

    for n in range(5, limit + 1):
        if sieve[n]:
            primes.append(n)

    return primes

# Найдём 10001-е простое
def find_10001_prime():
    primes = sieve_of_atkin(200000)
    return primes[10000]

print(find_10001_prime())