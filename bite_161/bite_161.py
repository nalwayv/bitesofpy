""" 
Bite 161: Count the number of files and directories
"""
import os
from typing import Tuple


def count_dirs_and_files(directory='.') -> Tuple[int, int]:
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    
    Paramiters:
    -----------
        directory (str):
            file path

    Returns:
    --------
        Tuple[int, int]:
            number of directory's and files
    """
    files = []
    dirs = []
    
    for _, _dir, _file in os.walk(os.path.abspath(directory)):
        if _dir:
            dirs += _dir
        if _file:
            files += _file

    return (len(dirs), len(files))
