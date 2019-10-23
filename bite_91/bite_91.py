""" 
Bite 91: Matching multiple strings
"""
VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    if not input_str:
        return False
    return all(
        [char in "".join([VOWELS, VOWELS.upper()]) for char in input_str])


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    if not input_str:
        return False
    return any(
        [char in "".join([PYTHON, PYTHON.upper()]) for char in input_str])


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    if not input_str:
        return False
    return any([char.isdigit() for char in input_str])
