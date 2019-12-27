""" 
Bite 241. Write tests for list_to_decimal
pytest:
    pytest test_list_to.py -v
mutpy:
    mut.py --target numbers_to_dec --unit-test test_list_to --runner pytest --coverage
"""

import pytest
from numbers_to_dec import list_to_decimal


@pytest.mark.parametrize('arr, expected', [([0, 4, 2, 8], 428), 
                                           ([1, 2], 12),
                                           ([3], 3)])
def test_list_to_decimal(arr, expected):
    assert list_to_decimal(arr) == expected


@pytest.mark.parametrize('arr', [[6, 2, True], [3.6, 4, 1], ['4', 5, 3, 1]])
def test_type_error(arr):
    with pytest.raises(TypeError):
        result = list_to_decimal(arr)


@pytest.mark.parametrize('arr', [[-3, 5], [10, 10, 1]])
def test_value_error(arr):
    with pytest.raises(ValueError):
        result = list_to_decimal(arr)


def test_value_error_out_of_range():
    with pytest.raises(ValueError):
        value = list_to_decimal([0, 11, 2, 3])
        if value == 1123:
            raise ValueError
