""" 
Bite 25. No promo twice, keep state in a class 
"""
import random

BITES = {
    6: 'PyBites Die Hard',
    7: 'Parsing dates from logs',
    9: 'Palindromes',
    10: 'Practice exceptions',
    11: 'Enrich a class with dunder methods',
    12: 'Write a user validation function',
    13: 'Convert dict in namedtuple/json',
    14: 'Generate a table of n sequences',
    15: 'Enumerate 2 sequences',
    16: 'Special PyBites date generator',
    17: 'Form teams from a group of friends',
    18: 'Find the most common word',
    19: 'Write a simple property',
    20: 'Write a context manager',
    21: 'Query a nested data structure'
}
bites_done = {6, 10, 16, 18, 21}


# CUSTOM ERROR
class NoBitesAvailable(Exception):
    pass


class Promo:
    def __init__(self, bites_done=bites_done):
        self.bites_done = bites_done

    def _pick_random_bite(self) -> int:
        """_pick_random_bite
        
        Returns
        -------
        int
            random number from BITES
        
        Raises
        ------
        NoBitesAvailable:
            no more bites
        """
        if len(self.bites_done) == len(BITES):
            raise NoBitesAvailable('no more bites')
        allowed = list({key for key in BITES.keys()} - self.bites_done)
        return random.choice(allowed)

    def new_bite(self) -> int:
        """new_bite
        
        Returns
        -------
        int:
            BITES number that was available
        """
        num = self._pick_random_bite()
        # update used bites
        self.bites_done.add(num)
        return num


if __name__ == "__main__":
    promo = Promo(bites_done)
    for key, item in BITES.items():
        try:
            ok1 = promo.new_bite()
            print(ok1)
        except NoBitesAvailable as err:
            print(err)
            break
    print('done A')

    # #  No more BITES
    # promo2 = Promo(bites_done)
    # for key, item in BITES.items():
    #     try:
    #         ok1 = promo2.new_bite()
    #         print(ok1)
    #     except NoBitesAvailable as err:
    #         print(err)
    #         break
    # print('done B')