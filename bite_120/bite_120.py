"""
Bite 120: 
"""
from functools import wraps


def int_args(func):
    """int_args
    
    check if all passed in func's *args aree of type int 
    and positive
    """
    # complete this decorator
    @wraps(func)
    def inner_wrap(*args):
        """inner_wrap
        
        Parameters
        ----------
        func: 
            function that takes int args
        
        Returns
        -------
        func: 
            function with args if checks were passed
        
        Raises
        ------
        TypeError:
            a not int was passed into args
        ValueError:
            a negative int was passed into args
        """
        if not all([isinstance(i, int) for i in args]):
            raise TypeError('a not int was passed')

        if not all([i >= 0 for i in args]):
            raise ValueError('a negative int was passed')

        return func(*args)

    return inner_wrap


# check args are positive ints
@int_args
def foo(*args):
    return sum(args)


if __name__ == "__main__":
    # print(foo(1, 2, 3, -4, 5))  # error
    # print(foo(1, 2, '3', 4, 5))  # error
    print(foo(1, 2, 3, 4, 5))  # ok
