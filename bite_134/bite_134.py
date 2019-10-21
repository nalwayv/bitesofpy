"""
bite 124 two sums
"""

NUMBERS = [
    2202, 9326, 1034, 4180, 1932, 8118, 7365, 7738, 6220, 3440, 1538, 7994,
    465, 6387, 7091, 9953, 35, 7298, 4364, 3749, 9686, 1675, 5201, 502, 366,
    417, 8871, 151, 6246, 3549, 6916, 476, 8645, 3633, 7175, 8124, 9059, 3819,
    5664, 3783, 3585, 7531, 4748, 353, 6819, 9117, 1639, 3046, 4857, 1981
]


def two_sums(numbers, target):
    nums_sorted = sorted(numbers)
    size = len(nums_sorted)
    low = 0
    high = size - 1

    while low <= high:
        calc = nums_sorted[low] + nums_sorted[high]

        if calc == target:
            idx_one = numbers.index(nums_sorted[low])
            idx_two = numbers.index(nums_sorted[high])
            return (idx_one, idx_two)

        if calc > target:
            high -= 1
        elif calc < target:
            low += 1

    return None
