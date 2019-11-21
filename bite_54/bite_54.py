""" 
Bite 54. Nicer formatting of a poem or text
"""
import textwrap

INDENTS = 4

shakespeare_unformatted = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """

shakespeare_formatted = """
To be, or not to be, that is the question:
    Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
    Or to take Arms against a Sea of troubles,
"""

rosetti_unformatted = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """

rosetti_formatted = """
Remember me when I am gone away,
    Gone far away into the silent land;
    When you can no more hold me by the hand,
Nor I half turn to go yet turning stay.
Remember me when no more day by day
    You tell me of our future that you planned:
    Only remember me; you understand
"""


def print_hanging_indents(poem: str):
    res = []
    check = False
    for t in [t.strip() for t in poem.splitlines(True)]:
        if t == '':
            check = True
            continue

        if not check:
            res.append(textwrap.indent(t, ' ' * INDENTS))
        else:
            res.append(t)
            check = False

    print('\n'.join(res))


if __name__ == "__main__":
    print_hanging_indents(shakespeare_unformatted)
    print("-"*50)
    print_hanging_indents(rosetti_unformatted)
