"""
Bite 114: Color class
"""
import os
import sys
import urllib.request
from typing import Tuple

from color_values import COLOR_NAMES  # noqa E402

# PREWORK (don't modify): import colors, save to temp file and import
# color_values_module = os.path.join(os.path.dirname(__file__), 'tmp', 'color_values.py')
# urllib.request.urlretrieve('https://bit.ly/2MSuu4z', color_values_module)
# sys.path.append(os.path.join(os.path.dirname(__file__), 'tmp')

# should be importable now


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """
    def __init__(self, color: str):

        self.name = None
        self.rgb = None

        if color.upper() in COLOR_NAMES:
            self.name = color.lower()
            self.rgb = COLOR_NAMES[color.upper()]

    @classmethod
    def hex2rgb(cls, hex: str) -> Tuple[int, int, int]:
        """Class method that converts a hex value into an rgb one"""
        #  '#ffffff'
        if len(hex) < 7:
            raise ValueError(f"too small {hex}")

        try:
            # split
            v1 = [f"0x{hex[i:i + 2]}" for i in range(1, len(hex) - 1, 2)]
            # convert to base 16
            result = [int(v, 16) for v in v1]
            return tuple(result)
        except ValueError:
            raise ValueError(f"failed to hex 2 rgb: {hex}")

    @classmethod
    def rgb2hex(cls, rgb: Tuple[int, int, int]) -> str:
        """Class method that converts an rgb value into a hex one"""
        # using result from bite 86
        if not isinstance(rgb, (tuple, list)):
            raise ValueError("wrong type")

        RED = 16
        GREEN = 8
        BLUE = 0
        r, g, b = rgb

        # out of range
        if r < 0 or r >= 256 or g < 0 or g >= 256 or b < 0 or b >= 256:
            raise ValueError("out of range")

        hex_it = hex((r << RED) + (g << GREEN) + (b << BLUE))[2:]

        if len(hex_it) < 6:
            return f"#{'0'*(6-len(hex_it))}{hex_it}".lower()
        return f"#{hex_it}".lower()

    def __repr__(self):
        """Returns the repl of the object"""
        if self.rgb is None:
            return "Color('Unknown')"
        return f"Color('{self.name}')"

    def __str__(self):
        """Returns the string value of the color object"""

        if self.rgb is None:
            return "Unknown"
        return f"{self.rgb}"
