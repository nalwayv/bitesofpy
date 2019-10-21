"""
Bite 84: Flatten lists recursively (Droste Bite)
Complete flatten that takes a list of lists 
(which can have lists ad infinitum) and flatten them into a one dimensional list.

So this input:

[1, [2, 3], [4, 5, [6, 7, [8, 9, 10]]]]

... should generate this output:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""


def flatten(list_of_lists):
    """flattern
    
    Parameters
    ----------
    list_of_lists : list
        list of lists or tuples
    
    Returns
    -------
    list
        list of flattern values
    """
    result = []

    def inner_flattern(v):
        """inner_flattern - recursive"""
        if len(v) == 0:
            return

        if isinstance(v[0], list) or isinstance(v[0], tuple):
            inner_flattern(v[0])
        else:
            result.append(v[0])

        inner_flattern(v[1:])

    # - results
    inner_flattern(list_of_lists)
    return result
