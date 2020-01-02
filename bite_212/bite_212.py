"""
Bite 212. Suppressing exceptions
"""
from contextlib import suppress
from typing import List, Any, Iterator


def sum_numbers(numbers: List[Any]) -> Iterator[Any]:
    """This generator divides each nummber by its consecutive number.
       So if it gets passed in [4, 2, 1] it yields 4/2 and 2/1.
       It ignores ZeroDivisionError and TypeError exceptions (latter happens
       when a string or other non-numeric data type is in numbers)

       Task: use contextlib's suppress twice to make the code below more concise.
    """
    for i, j in zip(numbers, numbers[1:]):
        # replace the block below
        with suppress(ZeroDivisionError), suppress(TypeError):
            yield i / j


if __name__ == "__main__":
    expected = [0.5, 0.0, 0.8, 0.4166666666666667]
    actual = list(sum_numbers([1, 2, 0, 4, 5, 12, 'a', 3]))
    print(actual == expected)