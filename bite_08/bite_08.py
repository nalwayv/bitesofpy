""" 
Bite 08
"""
def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    if n == 0:
        return string
    
    if n > 0:
        for i in range(n):
            string = f"{string[1:]}{string[:1]}"
    else:
        for i in range(0, n, -1):
            string = f"{string[-1:]}{string[:-1]}"

    return string
