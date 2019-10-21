"""
Bite 199
"""

class Person:
    def __init__(self):
        self.msg = "I am"
        self.person_msg = self.msg + " a person"
    def __str__(self):
        return self.person_msg

class Mother(Person):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return self.person_msg + " and a awesome mom"

class Father(Person):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return self.person_msg + " and a cool daddy"

class Child(Father,Mother):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return self.msg + " the coolest kid"
