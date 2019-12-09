""" 
Bite 217. Capture stdout
"""
from contextlib import redirect_stdout
from io import StringIO
from types import BuiltinFunctionType


def get_len_help_text(builtin: BuiltinFunctionType) -> int:
    """Receives a builtin, and returns the length of its help text.
       You need to redirect stdout from the help builtin.
       If the the object passed in is not a builtin, raise a ValueError.
    """
    if not isinstance(builtin, BuiltinFunctionType):
        raise ValueError('not a builtinFunctionType')

    with StringIO() as buf:

        with redirect_stdout(buf):
            help(builtin)

        res = len(buf.getvalue())
        print(res)


if __name__ == "__main__":
    get_len_help_text(max)
    get_len_help_text(pow)
