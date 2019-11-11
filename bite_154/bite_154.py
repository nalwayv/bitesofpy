"""
Bite 154. Write your own Data Class
"""
from dataclasses import dataclass, field


@dataclass(order=True)
class Bite:
    number: int = field(default=0)
    title: str = field(default="")
    level: str = field(default="Beginner")

    def __post_init__(self):
        self.title = self.title.capitalize()


if __name__ == "__main__":
    b1 = Bite(number=3, title="hello", level="c")
    b2 = Bite(number=1, title="hello", level="a")
    b3 = Bite(number=2, title="hello", level="b")
    data = sorted([b1, b2, b3])
    print(data)