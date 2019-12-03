""" 
Bite 200. Minecraft Enchantable Items
"""
import re
from collections import OrderedDict
from pathlib import Path
from typing import Dict, List

from bs4 import BeautifulSoup as Soup

FILE_PATH = Path('./tmp/minecraft.php')
URL = "https://www.digminecraft.com/lists/enchantment_list_pc.php"

NUMS = list(range(1, 11))
SYMS = 'I II III IV V VI VII VIII IX X'.split(" ")
ROMANS = {k: v for k, v in zip(SYMS, NUMS)}


class Enchantment:
    """Minecraft enchantment class
    
    Implements the following: 
        id_name, name, max_level, description, items
    """
    def __init__(self,
                 id_name: str,
                 name: str,
                 level: int,
                 desc: str,
                 items: List[str] = None):
        self.id_name = id_name
        self.name = name
        self.max_level = level
        self.description = desc
        self.items = [] if items is None else items

    def __str__(self):
        return f"{self.name} ({self.max_level}): {self.description}"


class Item:
    """Minecraft enchantable item class
    
    Implements the following: 
        name, enchantments
    """
    def __init__(self, name: str, enchantments: List["Enchantment"] = None):
        self.name = name
        self.enchantments = [] if enchantments is None else enchantments

    def __str__(self):
        data = sorted([(e.max_level, e.id_name) for e in self.enchantments],
                      key=lambda x: x[1])
        ent = '\n  '.join(f"[{e[0]}] {e[1]}" for e in data)
        name = self.name.replace("_", ' ').title()
        return f"{name}: \n  {ent}"


def get_soup(file=FILE_PATH) -> Soup:
    """Retrieves/takes source HTML and returns a BeautifulSoup object"""
    with file.open() as html_source:
        soup = Soup(html_source, "html.parser")
    return soup


def get_items(text: str) -> List[str]:
    """ get_items

    strips items from minecraft .png

    Example
    -------
    >>> text='/armor_recipes/images/enchanted_iron_helmet.png'
    >>> get_items(text)
    ['helmet]
    """
    pattern = r'(armor|axe|boots|bow|chestplate|crossbow|fishing_rod|shovel|helmet|pickaxe|sword|trident)'
    items_text = text.split("/")[-1]
    ok = re.findall(pattern, items_text)
    if ok:
        return ok
    return []


def generate_enchantments(soup: Soup) -> Dict[str, Enchantment]:
    """Generates a dictionary of Enchantment objects
    
    With the key being the id_name of the enchantment.
    """
    table: Soup = soup.select_one('table.std_table')

    enchantment_data = dict()

    # 0 is just non data
    for tr in table.findAll('tr')[1:]:
        name: str = tr.find('a').text
        id_name = tr.find('em').text
        level = tr.find('td').findNext('td').text
        description = tr.find('td', attrs={'class': 'hidden-xs'}).text
        items = get_items(tr.find('img')['data-src'])

        enchantment = Enchantment(id_name, name, ROMANS.get(level, 0),
                                  description, items)

        enchantment_data[id_name] = enchantment

    return enchantment_data


def generate_items(data: Dict[str, Enchantment]) -> Dict[str, Enchantment]:
    """Generates a dictionary of Item objects
    
    With the key being the item name.
    """
    dd = dict()

    for key, enchantment in data.items():
        for item_name in enchantment.items:
            # ever add to existing items enchantments list or add new Item
            if item_name in dd:
                dd[item_name].enchantments.append(enchantment)
            else:
                dd[item_name] = Item(item_name, [enchantment])

    return OrderedDict(sorted(dd.items()))


if __name__ == "__main__":
    soup_data = get_soup(FILE_PATH)
    gen_enchantments = generate_enchantments(soup_data)
    minecraft_items = generate_items(gen_enchantments)

    for item in minecraft_items:
        print(minecraft_items[item], "\n")
