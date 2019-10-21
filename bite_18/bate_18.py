"""
Bite 18: Find the most common word from potter.txt
"""

import os
import re
from collections import Counter
from typing import List, Optional, Tuple

# __CONSTS__

POTTER_FILE = os.path.join(os.path.dirname(__file__), "tmp", "potter.txt")
STOP_FILE = os.path.join(os.path.dirname(__file__), "tmp", "stop.txt")

# __FUNCS__


def stop_text() -> Tuple[bool, List[str]]:
    """stop_text

    Returns:
        Tuple[bool, List[str]]: True if file was fond plus a list of its text
                                else False and an empty list
    """
    stops: Optional[List[str]] = None
    ok = True

    try:
        with open(os.path.abspath(STOP_FILE)) as file:
            stops = file.readlines()
    except IOError as err:
        print(f"ERROR: {err}")
        ok = False

    return (ok, [s.strip() for s in stops])


def potter_text() -> Tuple[bool, List[str]]:
    """potter_text

    Returns:
        Tuple[bool, List[str]]: True if file was found and opened plus a list of all its text
                                else False and an empty list
    """
    text: Optional[List[str]] = None
    ok = True

    try:
        with open(os.path.abspath(POTTER_FILE), encoding="utf-8") as file:
            text = file.readlines()
    except IOError as err:
        print(f"ERROR: {err}")
        ok = False

    return (ok, [t.strip().lower() for t in text])


def pattern_match(msg: str) -> List[str]:
    """pattern_match

    Args:
        msg (str): string of words

    Returns:
        List[str]: words that matched the regex pattern
    """
    pattern = r"[a-zA-Z0-9_']+"
    check = re.compile(pattern)
    list_words = check.findall(msg)
    return list_words


def get_harry_most_common_word() -> Tuple[str, int]:
    """get_harry_most_common_word

    Returns:
        Tuple[str,int]: most common word and its frequency
    """
    potter_ok, potter_data = potter_text()
    if potter_ok:
        potter_match = pattern_match("".join(potter_data))

        if potter_match:
            stop_ok, stop_data = stop_text()

            if stop_ok:
                words = [
                    word for word in potter_match
                    if len(word) > 1 and word not in stop_data
                ]

                # max word
                words_counted = Counter(words)
                mc_word, mc_frequency = words_counted.most_common(1)[0]

                return (mc_word, mc_frequency)

    return ("", -1)

# if __name__ == "__main__":
#     out_put = get_harry_most_common_word()
#     print(out_put)
