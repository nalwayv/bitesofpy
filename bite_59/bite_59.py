"""
Bite 59: Create a multiplication table class of variable length
"""


class MultiplicationTable:
    def __init__(self, length: int):
        """Create a 2D self._table of (x, y) coordinates and
        their calculations (form of caching)

        Parameters
        ----------
        length : int
            table size
        """
        self.size = length
        self.numbers = []

        for i in range(1, length + 1):
            start = i
            nums = []
            for j in range(length):
                nums.append(start)
                start += i
            self.numbers += nums

        # 2d table
        # self.table  = [self.numbers[j:j+self.size] for j in range(0, self.size*self.size, self.size)]

    def __len__(self):
        """Returns the area of the table (len x* len y)"""
        return self.size * self.size

    def __str__(self):
        """Returns a string representation of the table"""

        return " | ".join([str(num) for num in self.numbers])

    def calc_cell(self, x: int, y: int) -> int:
        """Takes x and y coords and returns the (pre-calculated) result
        
        Parameters
        ----------
        x : int
            x coord
        y : int
            y coord
        
        Returns
        -------
        int
            number at x,y coord
        
        Raises
        ------
        IndexError
            out of range
        """
        # -1 as table is zero based
        cell_idx = (y - 1) * self.size + (x - 1)
        if cell_idx < 0 or cell_idx >= len(self.numbers):
            raise IndexError('out of range')

        return self.numbers[cell_idx]

