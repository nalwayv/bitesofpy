""" 
Bite 66
"""

def running_mean(sequence: list):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric

    Args:
    sequence (list): list or numbers
    
    Returns:
        list: list of numbers
    
    Raises:
        ZeroDivisionError
    """
    if not sequence:
        return []

    mean = []
    """
    [1]     = 1 / 1
    [1,2]   = 3 / 2 
    [1,2,3] = 6 / 3
    """
    for idx, num in enumerate(sequence):

        sum_total = sum(sequence[:(idx + 1)])
        result = sum_total / (idx + 1)

        mean.append(round(result, 2))

    return mean
