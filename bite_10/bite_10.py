"""
Bite 10: exceptions
"""
from math import floor

def d_floor(num, d=0):
    m=d**10
    return floor(num*m)/m
    
def positive_divide(numerator, denominator):
    try:
        if denominator == 0:
            return 0

        result = d_floor(numerator / denominator, 2)

        if result < 0:
            raise ValueError()
        else:
            return result

    except TypeError:
        raise TypeError()

# if __name__ == "__main__":
#     tests = [
#         (1, 2, 0.5),
#         (1, 0, 0),
#         (-1, -2, 0.5),
#         (1.5, 2, 0.75)
#     ]
#     for test in tests:
#         num, den, eq = test
#         if positive_divide(num, den) == eq:
#             print("yes")
#         else:
#             print("no")


