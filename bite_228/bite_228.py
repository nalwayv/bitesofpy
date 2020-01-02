"""
Bite 228. Create a Gravatar URL 
"""

import hashlib

GRAVATAR_URL = (
    "https://www.gravatar.com/avatar/{hashed_email}?s={size}&r=g&d=robohash")


def create_gravatar_url(email: str, size: int = 200) -> str:
    """Use GRAVATAR_URL above to create a gravatar URL.

       You need to create a hash of the email passed in.

       PHP example: https://en.gravatar.com/site/implement/hash/

       For Python check hashlib check out (md5 / hexdigest):
       https://docs.python.org/3/library/hashlib.html#hashlib.hash.hexdigest
    """
    h_digest = hashlib.md5(email.lower().strip().encode('utf8')).hexdigest()
    return GRAVATAR_URL.format(hashed_email=h_digest, size=size)


if __name__ == "__main__":
    tests = [("info@pybit.es", 200), ("info@pybit.es ", 200),
             ('info@pybit.ES', 40), ('support@pybit.es', 200),
             ('support@PYBIT.es', 200), (' support@pybit.es', 1000)]

    for e, s in tests:
        print(create_gravatar_url(e, s))
