""" 
Bite 132. Find the word with the most vowels
"""
from collections import Counter
from typing import Tuple

VOWELS = list('aeiou')

paragraphs = [
    ("Python is an easy to learn, powerful programming language."
     "It has efficient high-level data structures and a simple "
     "but effective approach to object-oriented programming. "
     "Python’s elegant syntax and dynamic typing, together with "
     "its interpreted nature, make it an ideal language for "
     "scripting and rapid application development in many areas "
     "on most platforms."),
    ("The Python interpreter and the extensive standard library "
     "are freely available in source or binary form for all major "
     "platforms from the Python Web site, https://www.python.org/, "
     "and may be freely distributed. The same site also contains "
     "distributions of and pointers to many free third party Python "
     "modules, programs and tools, and additional documentation."),
    ("The Python interpreter is easily extended with new functions "
     "and data types implemented in C or C++ (or other languages "
     "callable from C). Python is also suitable as an extension "
     "language for customizable applications."),
    ("This tutorial introduces the reader informally to the basic "
     "concepts and features of the Python language and system. "
     "It helps to have a Python interpreter handy for hands-on "
     "experience, but all examples are self-contained, so the "
     "tutorial can be read off-line as well."),
    ("For a description of standard objects and modules, see The "
     "Python Standard Library. The Python Language Reference gives "
     "a more formal definition of the language. To write extensions "
     "in C or C++, read Extending and Embedding the Python "
     "Interpreter and Python/C API Reference Manual. There are "
     "also several books covering Python in depth."),
    ("This tutorial does not attempt to be comprehensive and cover "
     "every single feature, or even every commonly used feature. "
     "Instead, it introduces many of Python’s most noteworthy "
     "features, and will give you a good idea of the language’s "
     "flavor and style. After reading it, you will be able to read and "
     "write Python modules and programs, and you will be ready to "
     "learn more about the various Python library modules described "
     "in The Python Standard Library.")
]


def get_word_max_vowels(text: str) -> Tuple[str, int]:
    """Get the case insensitive word in text that has most vowels.
       Return a tuple of the matching word and the vowel count, e.g.
       ('object-oriented', 6)
       
    Paramiters
    ----------
    text : str
        paragraph of text

    Returns
    -------
    Tuple[str, int] :
        word with most vowels and count
    """
    max_word = ''
    max_tally = -1
    
    for word in text.split(" "):
        tally = sum([val for key,val in Counter(word).items() if key in VOWELS])
        if tally > max_tally:
            max_tally = tally
            max_word = word

    return (max_word, max_tally)


if __name__ == "__main__":
    for text in paragraphs:
        word, vowels_count = (get_word_max_vowels(text))
        print(f"WORD: {word}, VOWELS: {vowels_count}")