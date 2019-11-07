"""
Bite 149. Sorting words with constraint
"""


WORDS = ("It's almost Holidays and PyBites wishes You a "
             "Merry Christmas and a Happy 2019").split()

WORDS2 = ("It was the twenty9th of October when it was questioned"
             "the meaning of nuMbers and weather hiding a number Inside"
             "tex56t should be treated as a word or another number").split()

WORDS3 = ("Let's see how4 this 1sorts, hope it works 4 this "
             "B1te 22 55abc abc55").split()

def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    def check_is_int(val):
        first=val[0]
        try:
            return isinstance(int(first), int)
        except ValueError:
             return False

    _ints=[word for word in words if check_is_int(word)]
    _strs=[word for word in words if not check_is_int(word)]


    return sorted(_strs, key=str.lower) + sorted(_ints, key=lambda x: x[0])

if __name__ == "__main__":
    ok = sort_words_case_insensitively(WORDS3)
    print(ok)