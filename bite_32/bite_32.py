""" 
Bite 32 deep copy dict objects
"""
import copy

items = [{
    'id': 1,
    'name': 'laptop',
    'value': 1000
}, {
    'id': 2,
    'name': 'chair',
    'value': 300
}, {
    'id': 3,
    'name': 'book',
    'value': 20
}]


def duplicate_items(items):
    return [copy.deepcopy(obj) for obj in items]


if __name__ == "__main__":
    v = duplicate_items(items)
    v[0]["id"] = 100
    print(v[0])
    print(items[0])
