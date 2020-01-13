""" 
Bite 254. Global vs local variables
"""

num_hundreds = -1


def sum_numbers(numbers: list) -> int:
    """Sums passed in numbers returning the total, also
       update the global variable num_hundreds with the amount
       of times 100 fits in total
    """
    global num_hundreds

    total = sum(numbers)
    num_hundreds += (total // 100)

    return total


if __name__ == "__main__":

    tests = [([], 0, -1), ([1, 2, 3], 6, -1), ([40, 50, 60], 150, 0),
             ([140, 50, 60], 250, 2), ([140, 150, 160], 450, 6),
             ([1140, 150, 160], 1450, 20)]

    for nums, expected, glob in tests:
        print(all([sum_numbers(nums) == expected, glob == num_hundreds]))
        print("-" * 45)
