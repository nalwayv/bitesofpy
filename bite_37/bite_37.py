""" 
Bite 37: Rewrite a for loop using recursion
Although you have to be careful using recursion it is one of those 
concepts you want to at least understand. 
It's also commonly used in coding interviews :)

In this beginner Bite we let you rewrite a simple countdown for loop 
using recursion. See countdown_for below, 
it produces the following output:
"""


def countdown_for(start=10):
    """countdown_for
    
    Parameters
    ----------
    start : int, optional
        [description], by default 10
    """
    for i in reversed(range(1, start + 1)):
        print(i)
    print('time is up')


def countdown_recursive(start=10):
    """countdown_recursive
    
    Parameters
    ----------
    start : int, optional
        by default 10
    
    Returns
    -------
    int
        number
    """
    if start <= 0:
        print('time is up')
        return start
    print(start)
    return countdown_recursive(start-1)
    