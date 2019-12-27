""" 
Bite 239. Test FizzBuzz
"""
from fizzbuzz import fizzbuzz
import pytest

# write one or more pytest functions below, they need to start with test_


@pytest.mark.parametrize('num, expected', [(1, 1), (3, 'Fizz'), (5, 'Buzz'),
                                           (15, 'Fizz Buzz')])
def test_fizzbuzz(num, expected) -> None:
    """ use of parameters to run more then one test at a time
    """
    assert fizzbuzz(num) == expected


def test_type_error_with_arg() -> None:
    with pytest.raises(TypeError):
        fizzbuzz('1')


def test_type_error_no_args() -> None:
    with pytest.raises(TypeError):
        fizzbuzz()