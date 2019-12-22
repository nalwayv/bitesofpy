"""
Bite 196. Create a JS-like dict object
"""
from typing import List, Any


class JsObject:
    """A Python dictionary that provides attribute-style access
       just like a JS object:

       obj = JsObject()
       obj.cool = True
       obj.foo = 'bar'

       Try this on a regular dict and you get
       AttributeError: 'dict' object has no attribute 'foo'
    """
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getitem__(self, key) -> Any:
        return self.__dict__.get(key)

    def __setitem__(self, key, value) -> None:
        self.__dict__[key] = value

    def __delitem__(self, key) -> None:
        self.__dict__.__delitem__(key)

    def __len__(self) -> int:
        return len(self.__dict__)

    def __contains__(self, key) -> bool:
        return key in self.__dict__

    def keys(self) -> List[Any]:
        return [k for k in self.__dict__.keys()]

    def values(self) -> List[Any]:
        return [k for k in self.__dict__.values()]

    def update(self, other) -> None:
        if not isinstance(other, dict):
            raise ValueError
        self.__dict__.update(other)


if __name__ == "__main__":
    foo = JsObject(a=1, b=2, c=3)

    test_dict = False
    test_js = False
    test_nested = True

    if test_dict:
        print(foo['a'] == 1)
        print(foo['b'] == 2)
        print(foo['c'] == 3)
        foo['d'] = 4
        print(len(foo) == 4)
        del foo['b']
        print(len(foo) == 3)
        print(foo.keys())
        print(foo.values())

    if test_js:
        print(foo.a == 1)
        print(foo.b == 2)
        print(foo.c == 3)
        foo.d = 4
        print(len(foo) == 4)
        del foo.b
        print(len(foo) == 3)
        print(foo.keys())
        print(foo.values())
        foo.update(dict(e=5))
        print(foo.e)

    if test_nested:
        foo.d = JsObject(e=5)
        print(foo.d.e)
        foo.d.e = JsObject(f=6)
        print(foo.d.e.f)
        