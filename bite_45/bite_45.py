"""
Bite 45: Keep a queue of last n items
"""

from typing import List


def my_queue(n=5):
    class Queue:

        def __init__(self):
            self.data=[]

        def append(self, value):
            """append - add to end"""
            if len(self.data) >= n:
                self.data.pop(0)
            self.data.append(value)

        def __iter__(self):
            for i in self.data:
                yield i

    return Queue()
