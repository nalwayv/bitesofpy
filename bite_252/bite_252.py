"""
Bite 252. Let's play with Pandas Series
"""
import pandas as pd
from string import ascii_lowercase


def float_series():
    """Returns a pandas Series containing floats"""
    return pd.Series([float(n) / 1000 for n in range(0, 1001)])

def alpha_series():
    """Returns a pandas Series containing floats"""
    dictionary = dict(zip(ascii_lowercase, range(1, 27)))
    return pd.Series(dictionary)

def return_at_index(ser: pd.Series, idx: int) -> object:
    """Return the Object at the given index of the Series
    If you want to be extra careful catch and raise an error if
       the index does not exist.
    """
    return ser.get(idx)


def get_slice(ser: pd.Series, start: int, end: int) -> pd.core.series.Series:
    """Return the slice of the given Series in the range between
    start and end.
    """
    return ser[start:end]
    

def get_slice_inclusive(ser: pd.Series, start: int,
                        end: int) -> pd.core.series.Series:
    """Return the slice of the given Series in the range between
    start and end inclusive.
    """
    return ser[start:end+1]


def return_head(ser: pd.Series, num: int) -> pd.core.series.Series:
    """Return the first num elements of the given Series.
    """
    return ser.head(n=num)


def return_tail(ser: pd.Series, num: int) -> pd.core.series.Series:
    """Return the last num elements of the given Series.
    """
    return ser.tail(n=num)


def get_index(ser: pd.Series) -> pd.core.indexes.base.Index:
    """Return all indexes of the given Series.
    """
    return ser.index


def get_values(ser: pd.Series) -> np.ndarray:
    """Return all the values of the given Series.
    """
    return ser.values


def get_every_second_indexes(ser: pd.Series,
                             even_index=True) -> pd.core.series.Series:
    """Return all rows where the index is either even or odd.
    If even_index is True return every index where idx % 2 == 0
    If even_index is False return every index where idx % 2 != 0
    Assume default indexing i.e. 0 -> n
    """
    n = len(ser.index)
    if even_index:
        return ser.drop(index=[i for i in range(n) if i&1 != 0])
    return ser.drop(index=[i for i in range(n) if i&1 == 0])
