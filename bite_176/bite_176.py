""" 
Bite 176
"""

WHITE, BLACK = ' ', '#'
def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    v1 = []
    v2 = []
    for i in range(size):
        if i % 2 == 0:
            v1.append(BLACK)
            v2.append(WHITE)
        else:
            v1.append(WHITE)
            v2.append(BLACK)

    flip = True
    for i in range(size):
        if not flip:
            print("".join(v1))
            flip = True
        else:
            print("".join(v2))
            flip = False
