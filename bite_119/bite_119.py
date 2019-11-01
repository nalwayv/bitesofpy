"""
 Bite 119. Xmas tree generator 
"""
from typing import List

def generate_xmas_tree(rows=10) -> List[str]:
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****

    Paramiters:
    -----------
        rows (int):
            number of rows to draw
    
    Returns:
    --------
        List[str]
    """
    gen_tree = []

    for i in range(1, rows+1):
        # blanks
        for j in range(i, rows):
            gen_tree.append(' ')
        # stars
        for k in range(i * 2 - 1):
            gen_tree.append('*')
        # end of line
        gen_tree.append('\n')

    return ''.join(gen_tree[:-1])


if __name__ == "__main__":
    print(generate_xmas_tree(3))
    print(len(generate_xmas_tree().split('\n')) == 10)
    print(len(generate_xmas_tree(5).split('\n')) == 5)
    print(len(generate_xmas_tree(20).split('\n')) == 20)

    print(generate_xmas_tree(3).count('*') == 9)
    print(generate_xmas_tree(5).count('*') == 25)
    print(generate_xmas_tree(20).count('*') == 400)
