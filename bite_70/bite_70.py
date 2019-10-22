"""
Bite 70: Create your own iterator
"""

from random import choice

COLORS = 'red blue green yellow brown purple'.split()

class EggCreator:
    def __init__(self, size: int):
        self.size = size
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number < self.size:
            self.number += 1
            return f"{choice(COLORS)} egg"
        else:
            raise StopIteration

# if __name__ == "__main__":
#     eggs_gen = EggCreator(5)

#     for egg in eggs_gen:
#         print(egg)