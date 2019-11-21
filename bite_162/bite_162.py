""" 
Bite 162. Vertically align output of counters
"""
import textwrap

HTML_SPACE = '&nbsp;'


def prefill_with_character(value, column_length=4, fill_char=HTML_SPACE):
    """Prepend value with fill_char for given column_length

    Parameters
    -----------
    value : int

    column_length : int

    fill_char : str

    Returns
    -------
    str
    """
    return f"{fill_char*(column_length - len(str(value)))}{value}"


if __name__ == "__main__":
    prefill_with_character(8, 5, HTML_SPACE)