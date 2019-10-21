"""
Bite 115: Count leading spaces
"""

def count_indents(text):
    """Takes a string and counts leading white spaces, return int count"""
    start = 0
    end = 0
    point = 0

    p = point

    while p < len(text):
        if not text[p].isspace():
            break
        p += 1

    start = point
    end = p
    point = p + 1
    return len(text[start:end])
