"""
Bite 208

In this Bite you complete find_number_pairs which receives a list of 
numbers and returns all the pairs that sum up N (default=10). 
Return this list of tuples from the function.

So in the most basic example if we pass in [2, 3, 5, 4, 6] it returns [(4, 6)] 
and if we give it [9, 1, 3, 8, 7] it returns [(9, 1), (3, 7)]. 
The tests check more scenarios (floats, other values of N, negative numbers).

Have fun and keep calm and code in Python

"""


def find_number_pairs(numbers, N=10):
    result = []

    for idx, num in enumerate(numbers):
        for other in numbers[idx + 1:]:
            if num + other == N:
                v = tuple([num, other])
                result.append(v)

    return result
