""" 
Bite 95. Subclass the dict built-in 
"""
from datetime import date

MSG = 'Hey {}, there are more people with your birthday!'


class BirthdayDict(dict):
    """Override dict to print a message every time a new person is added that has
       the same birthday (day+month) as somebody already in the dict"""
    def __init__(self, *args, **kwargs):
        self.update(*args, **kwargs)

    def __setitem__(self, name, birthday):
        found = False
        for date in self.values():
            if birthday == date or (birthday.day == date.day
                                    and birthday.month == date.month):
                found = True
                break

        if found:
            print(MSG.format(name))
        self.update({name: birthday})


if __name__ == "__main__":
    bd = BirthdayDict()
    bd['bob'] = date(1990, 5, 15)
    bd['sam'] = date(1990, 6, 15)