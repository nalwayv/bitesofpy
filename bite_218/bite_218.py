"""
Bite 218 sandwich decorator
"""
from typing import List, Callable
from functools import wraps


UPPER_SLICE = "=== Upper bread slice ==="
LOWER_SLICE = "=== Lower bread slice ==="


def sandwich(func: Callable[..., None]):
    """sandwich - sandwich decorator

    Returns
    -------
    func:
        function that returns None
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> None:
        """inner_sandwich

        Paramiters
        ----------
        *args:
            arguments
        **kwargs:
            key word arguments

        Returns
        -------
        None
        """
        print(UPPER_SLICE)
        func(*args, **kwargs)
        print(LOWER_SLICE)

    return wrapper


@sandwich
def add_ingredients(ingredients: List[str]) -> None:
    """add_ingredients

    Paramiters
    ----------
    ingredients:
        List[str]
    """
    print("/ ".join(ingredients))

