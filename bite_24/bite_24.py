""" 
Bite 24
"""
from abc import ABCMeta, abstractmethod, abstractproperty


class Challenge(metaclass=ABCMeta):
    """ISave. it does something? """

    @abstractmethod
    def __init__(self, number, title):
        self.number = number
        self.title = title

    @abstractmethod
    def verify(self, value):
        """verify 
        """
        raise NotImplementedError("missing verify")

    @property
    @abstractproperty
    def pretty_title(self):
        """pretty_title
        """
        raise NotImplementedError("missing pretty_title")

class BlogChallenge(Challenge):
    """BlogChallenge
    """

    def __init__(self, number, title, merged_prs):
        super().__init__(number, title)
        self.merge_prs = merged_prs

    def verify(self, value):
        """verify 
        """
        if not isinstance(value, int):
            return False
        return value in self.merge_prs

    @property
    def pretty_title(self):
        return f"PCC1 - {self.title}"


class BiteChallenge(Challenge):
    """BiteChallenge
    """
    def __init__(self, number, title, result):
        super().__init__(number, title)
        self.result = result

    def verify(self, value):
        """verify 
        """
        if not isinstance(value, str):
            return False
        return self.result == value
    
    @property
    def pretty_title(self):
        return f"Bite 24. {self.title}"
