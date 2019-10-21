"""
Bite 19:
"""
from datetime import datetime
from datetime import timedelta

NOW = datetime.now()


class Promo:
    def __init__(self,name:str, expires: datetime):
        self.name = name
        self.ex = expires
    
    @property
    def expired(self):
        date = NOW - self.ex
        return date.days > 0
