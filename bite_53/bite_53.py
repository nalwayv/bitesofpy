"""
Bite 53.  Convert text into multiple columns
"""
import re

COL_WIDTH = 20

TEXT = """My house is small but cosy.

It has a white kitchen and an empty fridge.

I have a very comfortable couch, people love to sit on it.

My mornings are filled with coffee and reading, if only I had a garden"""


def text_to_columns(text: str) -> str:
    """Split text (input arg) to columns, the amount of double
       newlines (\n\n) in text determines the amount of columns.
       Return a string with the column output like:
       line1\nline2\nline3\n ... etc ...
       See also the tests for more info."""

    lines = [l.strip() for l in text.splitlines() if l != ""]
    cols = text.count("\n\n")
    v1 = []

    for line in lines:
        start = 0
        end = 0
        point = 0
        n = len(line)
        v2 = []
        for idx in range(cols + 2):
            p = point + COL_WIDTH
            while p >= 0 and p < n:
                if line[point:p][-1] in [" ", "."]:
                    break
                p -= 1

            start = point
            end = p
            if idx >= 1:
                v2.append(line[start - 1:end].strip())
            else:
                v2.append(line[start:end].strip())
            point = p + 1

        v1.append(v2)

    v3 = []
    for row in list(zip(*v1)):
        v3.append("".join(line.ljust(COL_WIDTH + 5) for line in row))

    return "\n".join(v3)
