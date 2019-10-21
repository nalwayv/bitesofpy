"""
Bite 11 Enrich a class with dunder methods
"""
class Account:

    def __init__(self, name, start_balance=0):
        self.name = name
        self.start_balance = start_balance
        self._transactions = []

    @property
    def balance(self):
        return self.start_balance + sum(self._transactions)

    # add dunder methods below
    def __str__(self):
        return f"{self.name} account - balance: {self.balance}"

    def __add__(self, other:int):
        if not isinstance(other, int):
            raise ValueError()

        self._transactions.append(other)

        return self

    def __sub__(self, other:int):
        if not isinstance(other, int):
            raise ValueError()

        self._transactions.append(-other)

        return self

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, position:int):
        if position < 0 or position > len(self):
            raise IndexError()
        return self._transactions[position]

    def __eq__(self, other:"Account"):
        if not isinstance(other, Account):
            raise ValueError()
        return self.balance == other.balance

    def __lt__(self, other:"Account"):
        if not isinstance(other, Account):
            raise ValueError()
        return self.balance < other.balance

    def __le__(self, other:"Account"):
        if not isinstance(other, Account):
            raise ValueError()
        return self.balance <= other.balance

    def __gt__(self, other:"Account"):
        if not isinstance(other, Account):
            raise ValueError()
        return self.balance > other.balance

    def __ge__(self, other:"Account"):
        if not isinstance(other, Account):
            raise ValueError()
        return self.balance >= other.balance

    def __iter__(self):
        for i in self._transactions:
            yield i
