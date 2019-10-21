"""
Bite_255 swap case
"""
PYBITES = "pybites"


def convert_pybites_chars(text: str) -> str:
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string.
    """
    result = []

    for word in text.split(" "):
        chars = []

        for char in word:
            if char in f"{PYBITES}{PYBITES.upper()}":
                if char.isupper():
                    chars.append(char.lower())
                else:
                    chars.append(char.upper())
            else:
                chars.append(char)

        result.append("".join(chars))

    return " ".join(result)
