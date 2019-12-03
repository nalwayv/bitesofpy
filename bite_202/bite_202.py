""" 
Bite 202. Analyze some Bite stats data - part II
"""
import csv
from pathlib import Path
from re import match
from urllib.request import urlretrieve
from typing import Optional, List, Tuple

TMP = Path('./bite_202/tmp')
STATS = TMP / 'bites.csv'

# if not stats.exists():
#     urlretrieve('https://bit.ly/2MQyqXQ', stats)


def get_bite_id(description: str) -> Optional[str]:
    """get_bite_id
    
    Parameters
    ----------
    description : str
        csv bite description message
    
    Returns
    -------
    Optional[str]
        return bite str id or None
    """
    pattern = r'Bite.(\d+)'
    ok = match(pattern, description)
    if ok:
        return str(ok.group(1))
    return None


def get_most_complex_bites(N: int, stats: str) -> List[str]:
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    with stats.open(encoding="utf-8-sig") as csv_data:
        csv_reader = csv.reader(csv_data, delimiter=';')

        # [('88', 4.5), ('1', 5.0)]
        results: List[Tuple[str, float]] = []

        for idx, row in enumerate(csv_reader):
            if idx == 0:
                continue
            if row[1] != 'None':
                bite_id = get_bite_id(row[0])
                if bite_id is not None:
                    score = float(row[1])
                    results.append((bite_id, score))

        return [
            bite_id
            for bite_id, _ in sorted(results, key=lambda x: x[1], reverse=True)
        ][:N]
