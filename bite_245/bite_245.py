""" 
Bite 245. Xmas Tree 2.0
"""

STAR = "+"
LEAF = "*"
TRUNK = "|"

# Result Examples
default_tree = """
         +
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
    |||||||||||
    |||||||||||
"""

smaller_tree = """
  +
  *
 ***
*****
 |||
 |||
"""

def generate_improved_xmas_tree(rows=10) -> str:
    """Generate a xmas tree with a star (+), leafs (*) and a trunk (|)
       for given rows of leafs (default 10).
       For more information see the test and the bite description
    """

    tree_rows = []
    row_sizes = []

    for i in range(1, rows + 1):
        leafs = (i * 2) - 1
        space = ' ' * (rows - i)

        # star
        if i == 1:
            tree_rows.append(f"{space}+")

        # tree
        text = f"{space}{LEAF*leafs}"

        row_sizes.append(len(text))

        tree_rows.append(text)

    # trunk
    max_row_size = max(row_sizes)
    for trunk in range(2):
        width = max_row_size // 2 // 2
        trunks = max_row_size - (width * 2)
        tree_rows.append(f"{' '*width}{TRUNK*trunks}")

    return '\n'.join(tree_rows)


if __name__ == "__main__":
    xmax_tree = generate_improved_xmas_tree()
    print(xmax_tree)