"""
Bite 146. Rhombus generator
"""
STAR = '*'


def gen_rhombus(width):
    """Create a generator that yields the rows of a rhombus row
       by row. So if width = 5 it should generate the following
       rows one by one:

       gen = gen_rhombus(5)
       for row in gen:
           print(row)

        output:
          *
         ***
        *****
         ***
          *
    """
    mid = width // 2
    left = mid
    right = mid
    count = 1
    for i in range(width):

        yield f"{' '*left}{STAR*count}{' '*right}"

        if i < mid:
            right -= 1
            left -= 1
            count += 2
        else:
            right += 1
            left += 1
            count -= 2


if __name__ == "__main__":
    gen = gen_rhombus(11)
    for row in gen:
        print(row)