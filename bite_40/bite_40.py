"""
Bite 40 binary search
"""
from string import ascii_lowercase
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61]
ALPHABET = list(ascii_lowercase)


def in_order(arr):
    """in_order
    """
    size = len(arr)
    for idx in range(1, size):
        if arr[idx - 1] > arr[idx]:
            return False
    return True


def binary_search(sequence:list, target: int):
    """
    binary search
    """

    if not in_order(sequence):
        return None

    size = len(sequence)
    low = 0
    high = size

    while low <= high:
        mid = (high + low) // 2

        if mid < size:
            if sequence[mid] == target:
                return mid

            if target < sequence[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            break
    return None

# if __name__ == "__main__":
#     search_num = 18
#     search_char = 'z'

#     idx_num = binary_search(PRIMES, search_num)
#     print(f"{search_num} is at idx {idx_num}")

#     idx_abc_num = binary_search(ALPHABET, search_char)
#     print(f"{search_char} is at idx {idx_abc_num}")
