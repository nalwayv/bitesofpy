"""
Bite 68: remove punchuation from str
"""

def remove_punctuation(input_string: str):
    """Return a str with punctuation chars stripped out
    """

    PUNCHUATIONS = "!'#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    start = 0
    end = 0
    point = 0

    result = []
    n = len(input_string)

    while point < n:
        p = point

        while p < n:
            if input_string[p] in PUNCHUATIONS:
                break
            p += 1

        start = point
        end = p
        point = p + 1

        word = input_string[start:end]

        if word:
            result.append(word)

    return "".join(result)
