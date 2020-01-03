"""
Bite 250. PyBites URL Shortener
"""
from string import ascii_lowercase, ascii_uppercase, digits
from typing import Dict

CODEX: str = digits + ascii_lowercase + ascii_uppercase
BASE: int = len(CODEX)
# makeshift database record
LINKS: Dict[int, str] = {
    1: "https://pybit.es",
    45: "https://pybit.es/pages/articles.html",
    255: "http://pbreadinglist.herokuapp.com",
    600: "https://pybit.es/pages/challenges.html",
    874: "https://stackoverflow.com",
}
SITE: str = "https://pybit.es"

# error messages
INVALID = "Not a valid PyBites shortened url"
NO_RECORD = "Not a valid shortened url"


def encode(record: int) -> str:
    """Encodes an integer into Base62"""
    div62, mod62 = divmod(record, 62)

    if mod62 >= len(CODEX):
        raise IndexError

    result = [CODEX[mod62]]

    while div62:
        div62, rem = divmod(div62, 62)
        result = [CODEX[rem]] + result

    return ''.join(result)


def decode(short_url: str) -> int:
    """Decodes the Base62 string into a Base10 integer"""
    val = 0
    for char in short_url:
        codex_idx = CODEX.find(char)
        if codex_idx >= 0:
            val = 62 * val + codex_idx
    return val


def redirect(url: str) -> str:
    """Retrieves URL from shortened DB (LINKS)

    1. Check for valid domain
    2. Check if record exists
    3. Return URL stored in LINKS or proper message
    """
    if url[:len(SITE)] != SITE:
        return INVALID

    if '/' in url:
        end_url = url.split('/')[-1]
        decode_result = decode(end_url)
        if decode_result in LINKS:
            return LINKS[decode_result]

    return NO_RECORD


def shorten_url(url: str, next_record: int) -> str:
    """Shortens URL and updates the LINKS DB

    1. Encode next_record
    2. Adds url to LINKS
    3. Return shortened URL
    """
    encode_result = encode(next_record)
    short_url = f'{SITE}/{encode_result}'
    
    # add to links
    if next_record not in LINKS:
        LINKS[next_record] = url
    
    return short_url
