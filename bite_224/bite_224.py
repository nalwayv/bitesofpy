""" 
Bite 224. Get sentences from a text 
"""
import re
import string

TEXT = """
PyBites was founded 19th of December 2016. That means that today,
14th of October 2019 we are 1029 days old. Time flies when you code
in Python. Anyways, good luck with this Bite. What is your favorite editor?
"""  # contains 5 sentences

TEXT_WITH_DOTS = """
We are looking forward attending the next Pycon in the U.S.A.
in 2020. Hope you do so too. There is no better Python networking
event than Pycon. Meet awesome people and get inspired. Btw this
dot (.) should not end this sentence, the next one should. Have fun!
"""  # contains 6 sentences


def get_sentences(text):
    """Return a list of sentences as extracted from the text passed in.
       A sentence starts with [A-Z] and ends with [.?!]"""

    start = 0
    end = 0
    p0 = 0

    n = len(text)
    result = []

    while start < n:
        p1 = p0
        while p1 < n:
            if text[p1] == '.':
                # check behind
                check = f'{string.ascii_uppercase}{string.punctuation}'
                if text[p1 - 1] not in check:
                    break
            p1 += 1
        
        start = p0
        end = p1
        new_text = text[start:end].strip().replace('\n', ' ')
        p0 = p1 + 1

        # add . if needed
        if new_text:
            if new_text[-1:] not in ['?', '!']:
                result.append(new_text + '.')
            else:
                result.append(new_text)

    return result


if __name__ == "__main__":
    for line in get_sentences(TEXT):
        print(line)

    print("-" * 45)

    for line in get_sentences(TEXT_WITH_DOTS):
        print(line)
