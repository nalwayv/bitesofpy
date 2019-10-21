""" 
Bite 152: Manipulate string decorator
"""
from functools import wraps
import re

DEFAULT_TEXT = ['Hello world', 'Welcome to PyBites', 'Decorators for fun and profit']
DOT = '.'

def strip_range(start, end):
    """Decorator that replaces characters of a text by dots, from 'start'
       (inclusive) to 'end' (exclusive) = like range.

        So applying this decorator on a function like this and 'text'
        being 'Hello world' it would convert it into 'Hel.. world' when
        applied like this:

        @strip_range(3, 5)
        def gen_output(text):
            return text
    """
    def wrapper(func):
        @wraps(func)
        def inner_wrap(text):
            chars = ""
            
            start2 = 0 if start < 0 else start
            end2 = 0 if end < 0 else end

            if start2 > end2:
                chars = text[end2:start2]
            else:
                chars = text[start2:end2]

            res = re.sub(chars, DOT * len(chars), text)
            return func(res)

        return inner_wrap

    return wrapper


@strip_range(4, 8)
def get_output(text):
    print(text)
