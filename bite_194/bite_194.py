"""
Bite 194. Add caching to a Fibonacci function
"""
from functools import lru_cache


@lru_cache(maxsize=None)
def cached_fib(n: int) -> int:
    """cached_fib

    using functools lru_cache with a  simple fibonacci

    Parameters
    ----------
    n : int
        fibonacci at n = ?

    Returns
    -------
    int
       the fibonacci value
    """
    if n < 2:
        return n

    num_a, num_b = 0, 1
    for _ in range(1, n):
        num_a, num_b = num_b, num_a + num_b
    return num_b


if __name__ == "__main__":
    for i in range(7):
        value = cached_fib(i)
        print(value)
