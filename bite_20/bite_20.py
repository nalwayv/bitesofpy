""" 
Bite 20. Write a context manager 
"""


class Account:
    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class
    # into a 'rollback' context manager

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):

        if self.balance < 0:
            st = sorted(self._transactions, reverse=True)

            while sum(st) < 0:
                st.pop()
            self._transactions = st

        return self


if __name__ == "__main__":
    account = Account()
    with account as acc:
        acc + 10
    print(account.balance)