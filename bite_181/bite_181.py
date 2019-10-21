"""
Bite_181 keep list sorted upon insert.
"""

class OrderedList:
    """OrderedList
    """
    def __init__(self):
        self._numbers = []

    def __str__(self):
        return ", ".join(str(num) for num in self._numbers)

    def add(self, num: int):
        """add - add values to ordered list

        Parameters
        ----------
        num: int
            value to be added
        """
        if not self._numbers:
            self._numbers.append(num)
        else:
            idx = self._bsearch(num)
            self._numbers.insert(idx, num)

            # check
            ok = self._is_inorder()
            if not ok:
                raise Exception("rule broken as list is not in order!")

    def _is_inorder(self) -> bool:
        """_is_inorder - check ordered list is in order!

        Returns
        -------
        bool:
            is in order or not
        """
        size = len(self._numbers)
        for i in range(1, size):
            if self._numbers[i - 1] > self._numbers[i]:
                return False
        return True

    def _bsearch(self, num: int) -> int:
        """_bsearch

        Parameters
        ----------
        num: int
            value

        Returns
        -------
        int:
            idx
        """
        size = len(self._numbers)
        high = size
        low = 0

        while low <= high:

            mid = (high + low) // 2

            if mid < size:
                # same value
                if self._numbers[mid] == num:
                    return mid

                # high/low
                if num < self._numbers[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                break
        # just return lowest idx
        return low

# if __name__ == "__main__":
#     order = OrderedList()
#     for num in [10, 9, 16, 2, 7, 1, 5]:
#         order.add(num)
#     print(order)
