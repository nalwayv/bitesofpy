"""
Bite 158 list buit-in
"""
from decimal import Decimal


class IntList(list):
    """IntList
    """
    def __init__(self, vals):
        self.values = []

        for val in vals:
            self._check_add(val)

    def __str__(self):
        """__str__
        """
        return f"{self.values}"

    def __add__(self, other):
        """__add__ - override +
        """
        if not isinstance(other, list):
            raise TypeError()

        self.append(other)
        return self

    def __eq__(self, other):
        if not isinstance(other, list):
            return False
        return self.values == other

    def __iadd__(self, other):
        """__add__ - override +
        """
        if not isinstance(other, list):
            raise TypeError()

        self.append(other)
        return self

    def _int_or_float(self, value):
        """_int_or_float - checks if a value is of type int or a float
        """
        return isinstance(value, (int, float, Decimal))

    def _is_list(self, value):
        """_is_list - checks if value is of type list
        """
        return isinstance(value, list)

    def _check_add(self, value):
        if not self._int_or_float(value):
            raise TypeError()

        if isinstance(value,Decimal):
            value = float(value)

        self.values.append(value)

    def append(self, value):
        """append - adds to current values
        Examples
        --------
        >>> append(1)
        [1]
        >>> append([2, 3])
        [1, 2, 3]
        """
        # - list
        if self._is_list(value):
            for val in value:
                self._check_add(val)
            return
        # - single
        self._check_add(value)

    @property
    def mean(self):
        """mean - retruns mean of a list
        """
        result = round(sum(self.values) / len(self.values), 2)
        if not float.is_integer(result):
            return result
        return int(result)

    @property
    def median(self):
        """median - returns median of a list
        """
        size = len(self.values)
        sorted_cp = sorted(self.values[:])

        if size & 1 == 0:
            part_one = sorted_cp[(size - 1) // 2]
            part_two = sorted_cp[size // 2]
            return (part_one + part_two) / 2

        return sorted_cp[size // 2]


# if __name__ == "__main__":
#     my_list = IntList([1, 3, 5])
#     my_list += [1, 2, 3]
#     print(my_list == [1,3,5,1,2,3])
