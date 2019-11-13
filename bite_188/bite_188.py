from os import path
import statistics as st
import re
from typing import List

STATS = path.join(path.join(__file__), '..', 'tmp', 'testfiles_number_loc.txt')

STATS_OUTPUT = """
Basic statistics:
- count     : {count:7d}
- min       : {min_:7d}
- max       : {max_:7d}
- mean      : {mean:7.2f}

Population variance:
- pstdev    : {pstdev:7.2f}
- pvariance : {pvariance:7.2f}

Estimated variance for sample:
- count     : {sample_count:7.2f}
- stdev     : {sample_stdev:7.2f}
- variance  : {sample_variance:7.2f}
"""


def open_file(file_path: str) -> str:
    """open_file
    
    Parameters
    ----------
    file_path : str
        file path
    
    Returns
    -------
    str
        data from txt file
    """
    data: str = None
    with open(path.abspath(file_path)) as file:
        data = file.read()
    return data


def get_all_line_counts(data: str = STATS) -> List[int]:
    """Get all 186 line counts from the STATS file,
       returning a list of ints
    
    Parameters
    ----------
    data : str
        file path location

    Returns
    -------
    List[int] :
        list of ints
    """
    # TODO 1: get the 186 ints from downloaded STATS file

    data = open_file(data)
    numbers = []

    for line in data.splitlines():
        ok = re.match(r'^\d*', line.strip())
        if ok:
            numbers.append(ok.group(0).strip())

    return [int(n) for n in numbers]


def create_stats_report(data) -> str:
    # taking a sample for the last section
    sample = list(data)[::2]

    # TODO 2: complete this dict, use data list and
    # for the last 3 sample_ variables, use sample list
    stats = dict(
        count=len(data),
        min_=min(data),
        max_=max(data),
        mean=st.mean(data),
        pstdev=st.pstdev(data),
        pvariance=st.pvariance(data),
        sample_count=len(sample),
        sample_stdev=st.stdev(sample),
        sample_variance=st.variance(sample),
    )

    return STATS_OUTPUT.format(**stats)


if __name__ == "__main__":
    data = get_all_line_counts()
    data_output = create_stats_report(data)
    print(data_output)