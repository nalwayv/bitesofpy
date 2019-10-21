"""
Bite 03: Word Values

Calculate the dictionary word that would have the most value in Scrabble.
"""
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join(os.path.dirname(__file__), 'tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

SCRABBLE_SCORES = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {
    letter: score
    for score, letters in SCRABBLE_SCORES for letter in letters.split()
}


def load_words():
    """Load the words dictionary (DICTIONARY constant)
    into a list and return it
    """
    words = []
    file_path = os.path.abspath(DICTIONARY)

    try:
        with open(file_path, "r") as file:
            words = [line.rstrip("\n") for line in file]
    except IOError as err:
        print(f"file not found! - {err}")
        raise IOError()

    return words


def calc_word_value(word):
    """Given a word calculate its value
    using the LETTER_SCORES dict
    """
    tally = 0
    if not word:
        return tally

    for char in word.upper():
        if char in LETTER_SCORES:
            tally += LETTER_SCORES.get(char, 0)

    return tally


def max_word_value(words):
    """Given a list of words calculate the word with the maximum
    value and return it
    """
    max_score = -1
    max_word = ""
    for word in words:
        word_value = calc_word_value(word)

        if word_value > max_score:
            max_word = word
            max_score = word_value

    return max_word

# if __name__ == "__main__":
#     output = load_words()
#     if output:
#         print(output[0:10])
#         print(LETTER_SCORES)

#         for my_word in output[0:20]:
#             score = calc_word_value(my_word)
#             print(f"WORD: {my_word}, SCORE: {score}")

#         top_word = max_word_value(output[0:20])
#         print(top_word)
