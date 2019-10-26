"""
 Bite 179. Strip comments from Python code
"""
import re

# Text before and after

single_comment = '''
def hello_world():
    # A simple comment preceding a simple print statement
    print("Hello World")
'''

single_comment_after_strip = '''
def hello_world():
    print("Hello World")
'''

single_docstring = '''
def say_hello(name):
    """A simple function that says hello... Richie style"""
    print(f"Hello {name}, is it me you're looking for?")
'''

single_docstring_after_strip = '''
def say_hello(name):
    print(f"Hello {name}, is it me you're looking for?")
'''

class_with_method = '''
class SimpleClass:
    """Class docstrings go here."""

    def say_hello(self, name: str):
        """Class method docstrings go here."""
        print(f'Hello {name}')
'''

class_with_method_after_strip = '''
class SimpleClass:

    def say_hello(self, name: str):
        print(f'Hello {name}')
'''

multiline_docstring = '''
def __init__(self, name, sound, num_legs):
    """
    Parameters
    ----------
    name : str
        The name of the animal
    sound : str
        The sound the animal makes
    num_legs : int, optional
        The number of legs the animal (default is 4)
    """
    self.name = name
    self.sound = sound
    self.num_legs = num_legs
'''

multiline_docstring_after_strip = '''
def __init__(self, name, sound, num_legs):
    self.name = name
    self.sound = sound
    self.num_legs = num_legs
'''

code_bite_description = '''
"""this is
my awesome script
"""
# importing modules
import re

def hello(name):
    """my function docstring"""
    return f'hello {name}'  # my inline comment
'''

code_bite_description_after_strip = '''
import re

def hello(name):
    return f'hello {name}'
'''

class_three_indents = '''
class SimpleClass:
    """Class docstrings go here."""

    def say_hello(self, name: str):
        """Class method docstrings go here."""
        print(f'Hello {name}')

        def func_in_method(self):
            """Docstring with 3 indents and multiline
               should also be stripped
            """
            pass
'''

class_three_indents_after_strip = '''
class SimpleClass:

    def say_hello(self, name: str):
        print(f'Hello {name}')

        def func_in_method(self):
            pass
'''

false_positive = '''
def foo():
    # this is a comment
    print('this is not a #comment')
'''

false_positive_after_strip = '''
def foo():
    print('this is not a #comment')
'''


def strip_comments(code: str):
    """strip_comments
    
    Args:
        code (str): string of python code
    
    Returns:
        str: same code but with removed comments
    """
    pattern = r"\'{3,}[\s\S]*?\'{3,}|\"{3,}[\s\S]*?\"{3,}|\#.*\b$"
    stripped = re.sub(pattern, r'   ', code)
    v1 = [x for x in ''.join(stripped).splitlines() if not x.isspace()]

    v2 = []

    # remove some comments that were missed
    # not the best but it works for now
    for x in v1:
        if x:
            if x.strip()[0] != '#':
                v2.append(x)
        else:
            v2.append('')
    return '\n'.join(v2)


if __name__ == "__main__":

    tests = [(single_comment, single_comment_after_strip),
             (single_docstring, single_docstring_after_strip),
             (class_with_method, class_with_method_after_strip),
             (multiline_docstring, multiline_docstring_after_strip),
             (code_bite_description, code_bite_description_after_strip),
             (class_three_indents, class_three_indents_after_strip),
             (false_positive, false_positive_after_strip)]

    for a, b in tests:
        print(strip_comments(a).strip() == b.strip())