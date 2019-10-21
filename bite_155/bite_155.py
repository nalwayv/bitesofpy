"""
Bite 155: Split a string by spaces or quoted text
"""
import re
from typing import List

message = 'PyBites is a "A Community that Masters Python through Code Challenges"'


def split_words_and_quoted_text(text) -> List[str]:
    res = []
    for a, b in re.findall(r'"(.*?)"|(\w+)', text):
        if a:
            res.append(a.strip())
        if b:
            res.append(b.strip())
    return res

