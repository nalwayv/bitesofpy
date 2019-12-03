"""
Bite 76. The singledispatch countdown challenge
"""
from functools import singledispatch


def count_down_data(str_numbers: str):
    start = 0
    end = len(str_numbers)
    while start < end:
        print(str_numbers[start:end])
        end -= 1


@singledispatch
def count_down(data_type):
    # TODO: Learn how to use singledispatch!
    raise ValueError('no function overload for that data_type')


@count_down.register(str)
def _(data_type):
    count_down_data(data_type)


@count_down.register(int)
@count_down.register(float)
def _(data_type):
    str_data = str(data_type)
    count_down_data(str_data)


@count_down.register(list)
@count_down.register(tuple)
@count_down.register(set)
@count_down.register(range)
def _(data_type):
    str_data = ''.join([str(x) for x in data_type])
    count_down_data(str_data)


@count_down.register(dict)
def _(data_type):
    str_data = ''.join([str(x) for x in data_type.keys()])
    count_down_data(str_data)


if __name__ == "__main__":
    count_down('1234')
    # count_down(100.11)
    # count_down([1, 2, 3, 4, 5])
    # count_down((1, 2, 3, 4, 5))
    # count_down({1, 2, 3, 4, 5})
