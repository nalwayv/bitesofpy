""" 
Bite 214
"""

def countdown():
    """Write a generator that counts from 100 to 1"""
    count = 100
    while count > 0:
        yield count
        count -= 1
