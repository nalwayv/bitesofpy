"""
Bite 82. Define a Score Enum and customize it adding methods
"""
from enum import Enum

THUMBS_UP = '#'  # in case you go f-string ...

class Score(Enum):
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4
    CHEATED = 1

    def __str__(self):
        return f"{self.name} => {THUMBS_UP*1}"
    
    @classmethod
    def average(cls):
        arr = [v.value for v in list(cls)]
        return sum(arr)/len(arr)

if __name__ == "__main__":
    print(list(Score))
    print(Score.BEGINNER)
    Score.average()