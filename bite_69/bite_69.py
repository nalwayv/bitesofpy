""" 
Bite 69. Regex Fun - part II 
"""
import re
from typing import List


def has_timestamp(text: str) -> bool:
    """Return True if text has a timestamp of this format:
       2014-07-03T23:30:37"""
    # has_stamp = 'INFO 2014-07-03T23:27:51 Shutdown initiated.'
    if re.search(r'\d{4}-\d{2}-[0-9A-Z]+:[0-9]{2}:[0-9]{2}', text):
        return True
    return False


def is_integer(number: int) -> bool:
    """Return True if number is an integer"""
    if re.search(r'^[0-9]+$|^-[0-9]+$', str(number)):
        return True
    return False


def has_word_with_dashes(text: str) -> bool:
    """Returns True if text has one or more words with dashes"""
    if re.search(r'\w+-\w+', text):
        return True
    return False


def remove_all_parenthesis_words(text: str) -> str:
    """Return text but without any words or phrases in parenthesis:
       'Good morning (afternoon)' -> 'Good morning' (so don't forget
       leading spaces)"""

    pattern = re.compile(r'(\(.*?\))')
    return pattern.sub(r'~', text).replace(" ~", "")


def split_string_on_punctuation(text: str) -> List[str]:
    """Split on ?!.,; - e.g. "hi, how are you doing? blabla" ->
       ['hi', 'how are you doing', 'blabla']
       (make sure you strip trailing spaces)"""
    return [
        v.strip()
        for v in re.split(r'[!\"#$%&\'()*+,-.\/:;<=>?@\[\\\]^_`{|}~]', text)
        if v != ''
    ]


def remove_duplicate_spacing(text: str) -> str:
    """Replace multiple spaces by one space"""
    pattern = re.compile(r'\s{1,}')
    return pattern.sub(r' ', text)


def has_three_consecutive_vowels(word: str) -> bool:
    """Returns True if word has at least 3 consecutive vowels"""
    if re.search(r'[aeiou]{3,}', word):
        return True
    return False


def convert_emea_date_to_amer_date(date: str) -> str:
    """Convert dd/mm/yyyy (EMEA date format) to mm/dd/yyyy
       (AMER date format)"""

    _date = re.findall(r'(\d.*?)/(\d.*?)/(\d{4})', date)
    if _date:
        day, month, year = _date[0]
        return f"{month}/{day}/{year}"
    return 'none'


if __name__ == "__main__":
    print(f"- STAMP {'-'*45}")
    print(has_timestamp('INFO 2014-07-03T23:27:51 Shutdown initiated.'))
    print(has_timestamp('INFO 2014-06-01T13:28:51 Shutdown initiated.'))
    print(has_timestamp('INFO 2014-7-3T23:27:51 Shutdown initiated.'))
    print(has_timestamp('INFO 2014-07-03t23:27:1 Shutdown initiated.'))

    print(f"- INT {'-'*45}")
    print(is_integer(1))
    print(is_integer(-1))
    print(is_integer('str'))
    print(is_integer(1.1))

    print(f"- DASHES {'-'*45}")
    print(has_word_with_dashes('this Bite is self-contained'))
    print(has_word_with_dashes('the match ended in 1-1'))
    print(has_word_with_dashes('this Bite is not selfcontained'))
    print(has_word_with_dashes('the match ended in 1- 1'))

    print(f"- REPLACE {'-'*45}")
    for a, b in [('good morning (afternoon), how are you?',
                  'good morning, how are you?')]:
        print(remove_all_parenthesis_words(a) == b)

    for a, b in [('math (8.6) and science (9.1) where his strengths',
                  'math and science where his strengths')]:
        print(remove_all_parenthesis_words(a) == b)

    print(f"- SPLIT {'-'*45}")
    print(split_string_on_punctuation('hi, how are you doing? blabla'))
    print(
        split_string_on_punctuation(';String. with. punctuation characters!'))

    print(f"- DUPLICATE SPACEING {'-'*45}")
    print(
        remove_duplicate_spacing(
            'This is a   string with  too    much spacing'))

    print(f"- 3 VOWELS {'-'*45}")
    for word in ['beautiful', 'queueing', 'mountain', 'house']:
        print(has_three_consecutive_vowels(word))

    print(f"- DATE {'-'*45}")
    print(convert_emea_date_to_amer_date('31/03/2018'))
    print(convert_emea_date_to_amer_date('none'))