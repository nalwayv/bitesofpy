""" 
Bite 211. Write a retry decorator
"""
from functools import wraps
import random

MAX_RETRIES = 3


# Error
class MaxRetriesException(Exception):
    pass


def retry(func):
    """Complete this decorator, make sure
       you print the exception thrown"""
    # ... retry MAX_RETRIES times
    # ...
    # make sure you include this for testing:
    # except Exception as exc:
    #     print(exc)
    # ...
    # and use wraps to preserve docstring
    #
    @wraps(func)
    def wrapper(*args, **kwargs):

        tries = MAX_RETRIES
        while tries > 0:
            try:
                return func(*args, **kwargs)
            except Exception as err:
                print(err)

            tries -= 1

        raise MaxRetriesException

    return wrapper


@retry
def get_two_numbers(numbers):
    """Give a list of items pick 2 random ones,
       if both are not ints raise a ValueError
    """
    chosen = random.sample(numbers, 2)
    if not all(type(i) == int for i in chosen):
        raise ValueError('not all ints')


if __name__ == "__main__":
    for t in [['a', 'b', 'c'], [1, 2, 3]]:
        get_two_numbers(t)
