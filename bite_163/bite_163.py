"""
Bite 163. Which packages were upgraded?
"""
from typing import List, Tuple

OLD_REQS = """
certifi==2017.4.17
chardet==3.0.4
click==6.7
Faker==0.7.12
Flask==0.12.1
"""
NEW_REQS = """
certifi==2016.11.29
chardet==2.0.4
click==5.0
Faker==1.0.2
Flask==1.0.2
"""
OTHER_OLD_REQS = """
twilio==6.23.1
urllib3==1.21.1
Werkzeug==0.12.1
WTForms==1.19.0
"""
OTHER_NEW_REQS = """
twilio==6.3.0
urllib3==1.21.1
Werkzeug==0.14.1
WTForms==2.1
"""

def name_and_version(reqs: str) -> List[Tuple[str, Tuple[int, int, int]]]:
    """name_version

    return list of pakage name and version

    Parameters
    ----------
    reqs : str

    Returns
    -------
    List[Tuple[str, Tuple[int, int, int]]]:
        list of tuples that have pakage name and tuple of magor and minor versions

    Example
    --------
    >>> REQS = '''
        certifi==2017.4.17
        chardet==3.0.4
        click==6.7
        Faker==0.7.12
        Flask==0.12.1
        '''
    >>> name_and_version(REQS)
    [('certifi',(2017,4,17)),
     ('chardet',(3,0,4)),
     ('click',(6,7)),
     ('Faker',(0,7,12)),
     ('Flask',(0,12,1))]
    """
    res = []
    for line in reqs.splitlines()[1:]:
        name, version = line.split("==")
        res.append((name, tuple([int(v) for v in version.split(".")])))
    return res


def changed_dependencies(old_reqs: str, new_reqs: str) -> list:
    """Compare old vs new requirement multiline strings
       and return a list of dependencies that have been upgraded
       (have a newer version)
    """
    old = name_and_version(old_reqs)
    new = name_and_version(new_reqs)
    return [a[0] for a, b in zip(old, new) if a[1] < b[1]]


if __name__ == "__main__":
    changed_dependencies(OTHER_OLD_REQS, OTHER_NEW_REQS)