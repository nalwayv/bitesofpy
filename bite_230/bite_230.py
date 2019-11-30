"""
Bite 230. Thumbs up for operator overloading
"""

THUMBS_UP, THUMBS_DOWN = '👍', '👎'

class Thumbs:
    def __mul__(self, value):
        if value == 0:
            raise ValueError('Specify a number')

        sym = THUMBS_UP if value > 0 else THUMBS_DOWN

        if abs(value)>=4:
            return f"{sym} ({abs(value)}x)"
        return sym * abs(value)


    def __rmul__(self, value):
        return self.__mul__(value)

