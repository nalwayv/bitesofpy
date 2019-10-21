"""
Bite 110
"""
def divide_numbers(numerator, denominator):
    """For this exercise you can assume numerator and denominator are of type
       int/str/float.
       Try to convert numerator and denominator to int types, if that raises a
       ValueError reraise it. Following do the division and return the result.
       However if denominator is 0 catch the corresponding exception Python
       throws (cannot divide by 0), and return 0"""

    try:
        num = int(numerator)
        dem = int(denominator)

        return num / dem

    except ValueError:
        raise ValueError()

    except ZeroDivisionError:
        return 0

    return -1
