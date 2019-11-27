"""
Bite 190. Parse income distribution from Latin America XML
"""
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path
from typing import Dict, List

TMP = Path('bite_190/tmp')
COUNTRIES = TMP / 'countries.xml'

def get_income_distribution() -> Dict[str, List[str]]:
    """get_income_distribution
    
    - Read in the countries xml as stored in countries variable.
    - Parse the XML
    - Return a dict of:
      - keys : str = incomes (wb:incomeLevel)
      - values : List[str] = list of country names (wb:name)
    """
    with COUNTRIES.open() as xml_file:
        root = ET.parse(xml_file).getroot()
        names = []
        incomes = []
        data = defaultdict(list)

        for child in root.getiterator():
            name = None
            income = None
            if 'name' in child.tag:
                names.append(child.text)

            if 'incomeLevel' in child.tag:
                incomes.append(child.text)

        for name, income in zip(names, incomes):
            data[income].append(name)

        return data
