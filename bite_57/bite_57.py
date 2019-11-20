""" 
Bite 57. Create a simple calculator that receives command line arguments
"""
import argparse
from functools import reduce

"""TODO 1:
    Create a calculator that takes an operation and list of numbers.
    Perform the operation returning the result rounded to 2 decimals
"""

def calculator(operation, numbers):
    """TODO 1:
    Create a calculator that takes an operation and list of numbers.
    Perform the operation returning the result rounded to 2 decimals

    Parameters
    ----------
    operation : str
        
    numbers : list
    
    Returns
    -------
    float or int
    
    Raises
    ------
    Exception
        operation not found
    """

    if operation == 'add':
        res = round(sum(numbers), 2)

        if float.is_integer(res):
            return int(res)
        return res

    elif operation == 'sub':
        res = round(reduce(lambda x, y: x - y, numbers), 2)
        if float.is_integer(res):
            return int(res)
        return res

    elif operation == 'mul':
        res = round(reduce(lambda x, y: x * y, numbers), 2)
        if float.is_integer(res):
            return int(res)
        return res

    elif operation == 'div':
        res = round(reduce(lambda x, y: x / y, numbers), 2)
        if float.is_integer(res):
            return int(res)
        return res

    raise Exception('operation not found')


def create_parser():
    """TODO:
       Create an ArgumentParser adding the right arguments to pass the tests,
       returns a argparse.ArgumentParser object
    """
    parser = argparse.ArgumentParser(description='A simple calculator')

    parser.add_argument('-a',
                        '--add',
                        type=float,
                        dest='add',
                        action='store',
                        nargs='+',
                        help='Sums numbers')

    parser.add_argument('-s',
                        '--sub',
                        type=float,
                        dest='sub',
                        action='store',
                        nargs='+',
                        help='Subtracts numbers')

    parser.add_argument('-m',
                        '--mul',
                        type=float,
                        dest='mul',
                        action='store',
                        nargs='+',
                        help='Multiplies numbers')

    parser.add_argument('-d',
                        '--div',
                        type=float,
                        dest='div',
                        action='store',
                        nargs='+',
                        help='Divides numbers')

    return parser


def call_calculator(args=None, stdout=False):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    if args is None:
        args = parser.parse_args()

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():
        if numbers is None:
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res


if __name__ == '__main__':
    try:
        call_calculator(stdout=True)
    except Exception as err:
        print(f'error: {err}')