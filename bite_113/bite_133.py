""" 
Bite 113: Filter words with non-ascii characters 
"""
from typing import List
import string

PHRASES = [
    ('An preost wes on leoden, Laȝamon was ihoten', ['Laȝamon']),
    ('He wes Leovenaðes sone -- liðe him be Drihten', ['Leovenaðes', 'liðe']),
    ('He wonede at Ernleȝe at æðelen are chirechen', ['Ernleȝe', 'æðelen']),
    ('Uppen Sevarne staþe, sel þar him þuhte', ['staþe,', 'þar', 'þuhte']),
    ('Onfest Radestone, þer he bock radde', ['þer']),
    ('Fichier non trouvé', ['trouvé']),
    ('Over \u0e55\u0e57 57 flavours', ['๕๗']),
    ('Sí ... habrá que saber algo de Unicode, ¿no?', ['Sí', 'habrá', '¿no?']),
    ('This string only contains ascii words', []),
]

ENCODING = 'utf-8'

def extract_non_ascii_words(text: str) -> List[str]:
    """Filter a text returning a list of non-ascii words"""
    vals = [ord(char) for char in f"{string.ascii_letters}{string.punctuation}"]
    _max = max(vals)

    res = []
    for word in text.split(" "):
        if word:
            ok = all(ord(char) <= _max for char in word)
            if not ok:
                res.append(word.encode(ENCODING, 'ignore'))
    return res


if __name__ == "__main__":
    for a, _ in PHRASES:
        ok = extract_non_ascii_words(a)
        print(ok)
