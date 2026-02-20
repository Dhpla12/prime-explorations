"""
Prime number generation utilities.
"""

import math

def is_prime(n: int) -> bool:
    """Return True if n is prime, using optimised trial division."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(math.isqrt(n))
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

def generate_n_primes(n: int):
    """
    Generate the first n primes using sequential checking.
    Returns a list of the first n primes.
    """
    primes = []
    candidate = 2
    while len(primes) < n:
        if is_prime(candidate):
            primes.append(candidate)
        # After 2, only check odd numbers
        candidate += 1 if candidate == 2 else 2
    return primes

# Optional: Sieve of Eratosthenes (for completeness)
def sieve_of_eratosthenes(limit: int):
    """Return list of all primes <= limit."""
    if limit < 2:
        return []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.isqrt(limit)) + 1):
        if sieve[i]:
            step = i
            start = i * i
            sieve[start:limit+1:step] = [False] * ((limit - start) // step + 1)
    return [p for p, is_p in enumerate(sieve) if is_p]
