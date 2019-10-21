"""
Bite 99 Write an infinite sequence generator
"""

def sequence_generator():
    """sequence_generator - infinite sequence
    yields num then letter of the alphabet over and over and over.
    """
    point = 0
    num = 1
    abc = "abcdefghijklmnopqrstuvwxyz".upper()
    abc_max = 25

    while True:
        yield num
        num += 1
        yield abc[point]
        point += 1
        if point > abc_max:
            point = 0
            num = 1
