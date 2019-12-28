"""
Bite 238. Write tests for Fibonacci
"""
from fibonacci import fib
import pytest

@pytest.mark.parametrize('fib_num, result', [(2, 1), (4, 3), (10, 55)])
def test_fib(fib_num, result) -> None:
    assert fib(fib_num) == result

# test error
def test_fib_ValueError() -> None:
    with pytest.raises(ValueError):
        assert fib(-1) == 1
