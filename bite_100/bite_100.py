"""
Bite 100. Display the last part of a file (Unix tail) 
"""
import os
from typing import List

PATH = os.path.join(os.path.dirname(__file__), 'tmp', 'some_file.txt')


def open_file(file_path: str) -> List[str]:
    """open_file 
    
    Args:
        file_path (str): file path
    
    Returns:
        List[str]: 
    """
    abs_path = os.path.abspath(file_path)

    content = None
    with open(abs_path) as file:
        content = file.readlines()
    return content


def tail(filepath: str, n: int) -> List[str]:
    """tail

    Similate Unix' tail -n, read in filepath, parse it into a list,
    strip newlines and return a list of the last n lines

    Args:
        filepath (str): file path
        n (int): size

    Returns:
        List[str]:
    """
    lines = [line.strip() for line in open_file(filepath)]

    slice_idx = n * -1 if n > 0 else 0

    return lines[slice_idx:]
